#Author: Justin Law
#UNI: jhl2184

library(dplyr)
library(ggplot2)
library(scales)

raw <- read.csv('movielens\\ratings.csv',header=FALSE)

colnames(raw) <- c("uid","mid","rating","timestamp")
data <- select(raw, uid, mid)

# store the number of ratings per user
usercnt <- group_by(data, uid) %>% summarize(freq=n()) 

# store the number of ratings per movie
moviecnt <- group_by(data, mid) %>% 
  summarize(freq=n()) %>% arrange(desc(freq), mid) 

# rank the movies
movierank <- moviecnt %>% 
  mutate(rank = rownames(.)) %>%
  select(mid, rank)

movierank$rank <- as.numeric(movierank$rank)

# add the rank of the movies back to the dataset and arrange the data to be in ascending order of movie rank
data <- left_join(data, movierank, by="mid") %>% arrange(rank, uid) %>% 
  select(uid, rank) %>% left_join(usercnt, by="uid") %>% mutate(prob=1/freq)

# perform a cumulative sum on the percentage satisfaction of each user in ascending movie rank
data <- mutate(data, csum=0)
data$csum<-ave(data$prob, data$uid, FUN=cumsum)
data$csum<-round(data$csum,digits=10)

# calculate the CDF for 90% user satisfaction 
ninety <- mutate(data,satisfied=1 * (csum >= 0.9)) %>%
  filter(satisfied==1)
# remove the user after reaching satisfaction to prevent overcounting
ninety <- ninety[!duplicated(ninety$uid),]
ninety <- group_by(ninety,rank) %>% summarise(num=sum(satisfied)) %>%
  mutate(fraction=cumsum(num)/69878) %>%
  select(rank,fraction)

# calculate the CDF for 100% user satisfaction 
hundred <- mutate(data,satisfied=1 * (csum >= 1.0)) %>%
  filter(satisfied==1)
# remove the user after reaching satisfaction to prevent overcounting
hundred <- hundred[!duplicated(hundred$uid),]
hundred <- group_by(hundred,rank) %>% summarise(num=sum(satisfied)) %>%
  mutate(fraction=cumsum(num)/69878) %>%
  select(rank,fraction)

# add a data point at the last rank to account for missing ranks when removing users
ninety <- rbind(ninety,c(10677, 1.0))
hundred <- rbind(hundred,c(10677, 1.0))

ggplot() + 
  geom_line(data=hundred, aes(rank, fraction,color="100%")) + 
  geom_line(data=ninety, aes(rank, fraction, color="90%")) + 
  scale_y_continuous(breaks=0:10/10,labels=percent) +
  scale_x_continuous(breaks=0:11*1000) +
  scale_color_discrete(name="Satisfaction level") + 
  ggtitle("Anatomy of the Long Tail") + 
  xlab("Inventory Size") + 
  ylab("Fraction of Users Satisfied")