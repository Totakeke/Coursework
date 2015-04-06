library(shiny)
library(ggvis)
library(lubridate)

shinyUI(fixedPage(
  includeScript("chat.js"),
  theme="bootstrap.css",
  
  tags$div(class='titles',
    titlePanel("STATS"),
    h3("Buildings"),
    h4("number of buildings over time")
  ),
  
  fixedRow(

    column(8,
           ggvisOutput("ggvis")
           ),
    
    column(4,
           tags$div(class="pbuilds",
#            h4("Player 1"),
                    tags$div(class = "p1build",
                            strong("Totakeke"),
                            tableOutput("build1")),
                    tags$div(class = "p2build",
                            strong("Ms. Production"),
                            tableOutput("build2")),
                    tags$div(class = "p3build",
                            strong("Mr. Sabotage"),
                            tableOutput("build3")),
                    tags$div(class = "p4build",
                            strong("Ms. Launch"),
                            tableOutput("build4"))
                    )
    
  ),
  
  fixedRow(
    column(8,
           wellPanel(
             sliderInput("timebar",
                         "Time",
                         min = 0,
                         max = max(minute(plotdata$Time))+1,
                         value = max(minute(plotdata$Time))+1,
                         animate = animationOptions(interval=500),
                         step=0.5
                         )

           )
    ),
    column(4,
             uiOutput("chat")
           )
    )
    
  )
  )
)
