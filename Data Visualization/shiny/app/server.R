library(shiny)
library(dplyr)
library(lubridate)
library(ggvis)

data <- read.csv(file="offworldreplay.csv",head=TRUE,sep=",")
buildingtypes <- read.csv(file="buildings.csv",head=TRUE,sep=",")
buildcsum <-  read.csv(file="offworldreplaybuildsum.csv", head=TRUE, sep=",")
buildsum_mod <- read.csv(file="buildsum_mod.csv", head=TRUE, sep=",", stringsAsFactors = FALSE)

buildcsum$Time <- buildcsum$Time %>% format(format = "%M:%S") %>% as.POSIXct(format ="%M:%S")
buildsum_mod$Time <- buildsum_mod$Time %>% format(format = "%M:%S") %>% as.POSIXct(format ="%M:%S")
data$Time <- data$Time %>% format(format = "%M:%S") %>% as.POSIXct(format ="%M:%S")

buildingtypes$Image <- paste('<img src="', buildingtypes$Image, '" height=30 title="', buildingtypes$Building, '" />', sep ='')

plotdata <- select(data, Time, Buildings, Player, Message)
plotdata$Player <- factor(plotdata$Player, levels=c('Totakeke', 'Ms. Production', 'Mr. Sabotage', 'Ms. Launch'))

starttime <- head(plotdata$Time, 1)

color <- c('#379FA8', '#B82327', '#76A73E', '#E16823')
player <- unique(plotdata$Player)
playercolor <- data.frame(color, player)
plotdata<-left_join(plotdata, playercolor, c("Player"="player"))

colnames1 <- as.matrix(buildingtypes$Image)[1:10]
colnames2 <- as.matrix(buildingtypes$Image)[11:20] 

shinyServer(function(input, output) {
  
  timelim <- reactive({starttime + input$timebar*60})
  
  builddata <- reactive({buildcsum[buildcsum$Time <= timelim(),]})
  moddata <- reactive({buildsum_mod[buildsum_mod$Time <= timelim(),]})
  
  graphdata <- reactive({temp <- plotdata[plotdata$Time <= timelim(),]})
  
  graphdata %>% 
    ggvis(~Time, ~Buildings, stroke:=~color) %>% 
    layer_lines(strokeWidth:=2) %>%
  add_axis("x", 
           orient = "bottom", 
           tick_size_major=0, 
           format="%M", 
           title ="",
           properties = axis_props(
             axis = list(stroke="#545351",
                         strokeWidth=2.5),
             grid = list(stroke="#545351",
                         strokeWidth=0.5),
             labels = list(
               fill = "#555553",
               fontSize = 10,
               align = "left",
               dx = -1
             ),
           )) %>%
  add_axis("x",
           orient = "top",
           tick_size_major=0, 
           title = "",
           properties = axis_props(
             axis = list(stroke="#545351",
                         strokeWidth=2.5),
             grid = list(stroke="transparent"),
             labels = list(fill = "transparent"))) %>%
  add_axis("y",
           orient = "right",
           tick_size_major=0, 
           title = "",
           properties = axis_props(
             axis = list(stroke="#545351",
                         strokeWidth=2.5),
             grid = list(stroke="transparent"),
             labels = list(fill = "transparent"))) %>%
  add_axis("y", 
           orient = "left", 
           tick_size_major=0, 
           title = "",
           properties = axis_props(
             axis = list(stroke="#545351",
                         strokeWidth=2.5),
             grid = list(stroke="#545351",
                         strokeWidth=0.5),
             labels = list(
               fill = "#555553",
               fontSize = 10
             ),
           )) %>%
    hide_legend("fill") %>%
    hide_legend("stroke") %>%
    scale_datetime("x", domain = c(min(plotdata$Time), max(plotdata$Time)), expand=c(0,0)) %>%
    scale_numeric("y", domain = c(0, max(plotdata$Buildings)+7), expand=c(0,0),  nice = FALSE) %>% 
    set_options(width = 700, height = 500) %>%
    bind_shiny("ggvis", "ggvis_ui")
  
  output$build1 <- renderTable({
      player1 <- builddata() %>% filter(Player=="Totakeke") %>% select(-Player) %>% tail(1)
      mod1 <- moddata() %>% filter(Player=="Totakeke") %>% select(-Player) %>% tail(1)
      player1[2:21] <- paste0(mod1[,2:21],player1[,2:21],"</div>")
      build1 <- rbind(colnames1,
                      as.matrix(select(player1, 2:11)),
                      colnames2,
                  as.matrix(select(player1, 12:21)))
  rownames(build1)<-NULL
  build1
    },
  include.colnames=FALSE,
  include.rownames=FALSE,
  sanitize.text.function = function(x) x
  ) 

  output$build2 <- renderTable({
    player2 <- builddata() %>% filter(Player=="Ms. Production") %>% select(-Player) %>% tail(1)
    mod2 <- moddata() %>% filter(Player=="Ms. Production") %>% select(-Player) %>% tail(1)
    player2[2:21] <- paste0(mod2[,2:21],player2[,2:21],"</div>")
    build2 <- rbind(colnames1,
                    as.matrix(select(player2, 2:11)),
                    colnames2,
                    as.matrix(select(player2, 12:21)))
    rownames(build2)<-NULL
    build2
  },
  include.colnames=FALSE,
  include.rownames=FALSE,
  sanitize.text.function = function(x) x
  ) 
  
  output$build3 <- renderTable({
    player3 <- builddata() %>% filter(Player=="Mr. Sabotage") %>% select(-Player) %>% tail(1)
    mod3 <- moddata() %>% filter(Player=="Mr. Sabotage") %>% select(-Player) %>% tail(1)
    player3[2:21] <- paste0(mod3[,2:21],player3[,2:21],"</div>")
    build3 <- rbind(colnames1,
                    as.matrix(select(player3, 2:11)),
                    colnames2,
                    as.matrix(select(player3, 12:21)))
    rownames(build3)<-NULL
    build3
  },
  include.colnames=FALSE,
  include.rownames=FALSE,
  sanitize.text.function = function(x) x
  ) 

  output$build4 <- renderTable({
    player4 <- builddata() %>% filter(Player=="Ms. Launch") %>% select(-Player) %>% tail(1)
    mod4 <- moddata() %>% filter(Player=="Ms. Launch") %>% select(-Player) %>% tail(1)
    player4[2:21] <- paste0(mod4[,2:21],player4[,2:21],"</div>")
    build4 <- rbind(colnames1,
                    as.matrix(select(player4, 2:11)),
                    colnames2,
                    as.matrix(select(player4, 12:21)))
    rownames(build4)<-NULL
    build4
  },
  include.colnames=FALSE,
  include.rownames=FALSE,
  sanitize.text.function = function(x) x
  ) 

  output$chat <- renderUI({
    messages <- data[data$Time <= timelim(),]
    messages <- messages[!messages$Message=="", ]
    messages <- paste("[", strftime(messages$Time, format="%M:%S"), "] ", messages$Message, sep='')
    if (length(messages) > 1) {
      HTML(as.vector(c(messages[1],paste0("</br>", messages[2:length(messages)]))))
    }
    else {
      HTML(as.vector(messages))
    }    
  })
})

