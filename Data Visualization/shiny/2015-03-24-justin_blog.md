# Stat screen critique and Shiny visualization
Justin Law  
Tuesday, March 24, 2015  

## Graph Critique  

This graph critique will be focused more on the context of data visualization and the ability of the visualization to provide insight to its readers. The following two graphs depict stock prices and resource prices over time and are relatively simple to interpret.  

![Screenshot of a stock prices over time stats page](../assets/justin/images/2015-03-21_00001.jpg)

![Screenshot of a resource prices over time stats page](../assets/justin/images/2015-03-21_00002.jpg)

These two graphs originate from a strategy game called [Offworld Trading Company](http://www.offworldgame.com/) and are presented to players at the end of a game. Offworld Trading Company is a game about extracting resources and trading commodities on a shared market among players with the goal of buying out every other company. So in terms of the general concept of this game, this has an analog to real world stock markets and commodities trading and shouldn't be difficult to relate to.

There is also an interesting link between data visualization and games because at its core, all games are about taking in information that is presented to you and using that information to perform the best actions while operating under the rules of the game. In information rich games such as strategy games, balancing the amount of information to show players is important and an important consideration during game design. Displaying too much information would be overwhelming to new players while abstracting too much information would cause players to be unable to tell how their actions affect the consequences thus making gameplay confusing. So most game developers are already quite adept at visualizing data and balancing these two needs. However statistics or summary screens that appear after games have ended are still often an afterthought and often doesn't convey much meaningful information to players.

![Sometimes players just want to customize their interface to have as much data as possible](../assets/justin/images/dont-play-games-with-me-promises-and-pitfalls-of-gameful-design-77-1024.jpg) 
[Source](http://www.slideshare.net/dings/dont-play-games-with-me-promises-and-pitfalls-of-gameful-design)

So for these two graphs, the problem that they have is related to context. The considerations from real world analog where these types of charts are common does not apply because these markets have already ceased to exist when these graphs are presented to the player. They cannot be used to predict future stock prices and the resource price trends that are shown would not represent the same trends in another game due to the randomization of available resources. So to the players involved in the game, the graphs only tells the players what they already roughly know and it is meaningless for people who didn't participate. 

![Gameplay screenshot of a game in Offworld Trading Company](../assets/justin/images/2015-02-14_00002.jpg)

## Graph Improvement
### Main Graph

For the graph improvement, I propose a focus on graphing out the actions of the players rather than the consequences. This is not to replace the existing graphs above, but to complement them so that players can better understand how their actions affect the outcomes in the game.The two main decisions available to players in this game are constructing buildings to extract resources and trading commodities on the market for profit. It is also interesting to note here that while watching full replays of games are typically the method used for competitive players to improve, it is much more difficult to observe these two types of actions for this game because players can build buildings anywhere on the map, and purchasing or selling on the market by other players do not generate any visual cues. Hence, data visualization can also play a role here in providing understanding of what happened across all players rather than just through the point of view of a single player. 

As currently it does not seem possible to extract data out of the binary replay files, data has to be manually collected through viewing the replay from the point of view for each player. For this blog post I will only be focusing on constructing a number of buildings over time graph for the number of buildings players have built over time. Since the goal is to complement the existing graphs, creating a line grpah similar to the ones already exist was the most obvious action.

<!--html_preserve--><div id="plot_id986029526-container" class="ggvis-output-container">
<div id="plot_id986029526" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id986029526_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id986029526" data-renderer="svg">SVG</a>
 | 
<a id="plot_id986029526_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id986029526" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id986029526_download" class="ggvis-download" data-plot-id="plot_id986029526">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id986029526_spec = {
    "data": [
        {
            "name": ".0/group_by1/arrange2_flat",
            "format": {
                "type": "csv",
                "parse": {
                    "Time": "number",
                    "Buildings": "number"
                }
            },
            "values": "\"Player\",\"Time\",\"Buildings\"\n\"Mr. Sabotage\",1427342404000,0\n\"Mr. Sabotage\",1427342406000,1\n\"Mr. Sabotage\",1427342416000,2\n\"Mr. Sabotage\",1427342419000,3\n\"Mr. Sabotage\",1427342499000,4\n\"Mr. Sabotage\",1427342586000,5\n\"Mr. Sabotage\",1427342697000,5\n\"Mr. Sabotage\",1427342702000,6\n\"Mr. Sabotage\",1427342736000,7\n\"Mr. Sabotage\",1427342742000,8\n\"Mr. Sabotage\",1427342844000,9\n\"Mr. Sabotage\",1427342982000,9\n\"Mr. Sabotage\",1427342982000,10\n\"Mr. Sabotage\",1427342988000,11\n\"Mr. Sabotage\",1427343003000,12\n\"Mr. Sabotage\",1427343046000,13\n\"Mr. Sabotage\",1427343192000,13\n\"Mr. Sabotage\",1427343194000,14\n\"Mr. Sabotage\",1427343197000,15\n\"Mr. Sabotage\",1427343215000,16\n\"Mr. Sabotage\",1427343233000,0\n\"Ms. Launch\",1427342416000,0\n\"Ms. Launch\",1427342417000,1\n\"Ms. Launch\",1427342436000,2\n\"Ms. Launch\",1427342436000,3\n\"Ms. Launch\",1427342499000,4\n\"Ms. Launch\",1427342599000,4\n\"Ms. Launch\",1427342613000,5\n\"Ms. Launch\",1427342639000,6\n\"Ms. Launch\",1427342650000,7\n\"Ms. Launch\",1427342705000,6\n\"Ms. Launch\",1427342706000,7\n\"Ms. Launch\",1427343024000,7\n\"Ms. Launch\",1427343025000,8\n\"Ms. Launch\",1427343027000,9\n\"Ms. Launch\",1427343035000,10\n\"Ms. Launch\",1427343076000,9\n\"Ms. Launch\",1427343077000,10\n\"Ms. Launch\",1427343230000,10\n\"Ms. Launch\",1427343232000,11\n\"Ms. Launch\",1427343232000,12\n\"Ms. Launch\",1427343233000,13\n\"Ms. Launch\",1427343233000,14\n\"Ms. Launch\",1427343298000,15\n\"Ms. Launch\",1427343340000,15\n\"Ms. Launch\",1427343340000,16\n\"Ms. Launch\",1427343345000,0\n\"Ms. Production\",1427342417000,0\n\"Ms. Production\",1427342419000,1\n\"Ms. Production\",1427342419000,2\n\"Ms. Production\",1427342421000,3\n\"Ms. Production\",1427342467000,4\n\"Ms. Production\",1427342598000,4\n\"Ms. Production\",1427342620000,5\n\"Ms. Production\",1427342638000,6\n\"Ms. Production\",1427342642000,7\n\"Ms. Production\",1427342652000,8\n\"Ms. Production\",1427342672000,9\n\"Ms. Production\",1427342726000,10\n\"Ms. Production\",1427342798000,10\n\"Ms. Production\",1427342803000,11\n\"Ms. Production\",1427342807000,12\n\"Ms. Production\",1427342816000,13\n\"Ms. Production\",1427342818000,14\n\"Ms. Production\",1427342856000,13\n\"Ms. Production\",1427342857000,14\n\"Ms. Production\",1427342880000,15\n\"Ms. Production\",1427342970000,15\n\"Ms. Production\",1427342975000,16\n\"Ms. Production\",1427342978000,17\n\"Ms. Production\",1427342986000,18\n\"Ms. Production\",1427342994000,19\n\"Ms. Production\",1427342996000,20\n\"Ms. Production\",1427343033000,21\n\"Ms. Production\",1427343147000,21\n\"Ms. Production\",1427343151000,22\n\"Ms. Production\",1427343151000,23\n\"Ms. Production\",1427343159000,24\n\"Ms. Production\",1427343167000,25\n\"Ms. Production\",1427343177000,26\n\"Ms. Production\",1427343177000,27\n\"Ms. Production\",1427343237000,28\n\"Ms. Production\",1427343276000,27\n\"Ms. Production\",1427343277000,28\n\"Ms. Production\",1427343320000,27\n\"Ms. Production\",1427343321000,28\n\"Ms. Production\",1427343442000,0\n\"Totakeke\",1427342400000,0\n\"Totakeke\",1427342403000,1\n\"Totakeke\",1427342406000,2\n\"Totakeke\",1427342407000,3\n\"Totakeke\",1427342467000,3\n\"Totakeke\",1427342473000,4\n\"Totakeke\",1427342474000,5\n\"Totakeke\",1427342494000,6\n\"Totakeke\",1427342497000,7\n\"Totakeke\",1427342554000,6\n\"Totakeke\",1427342568000,7\n\"Totakeke\",1427342585000,6\n\"Totakeke\",1427342598000,7\n\"Totakeke\",1427342627000,7\n\"Totakeke\",1427342634000,8\n\"Totakeke\",1427342641000,9\n\"Totakeke\",1427342653000,10\n\"Totakeke\",1427342653000,11\n\"Totakeke\",1427342672000,12\n\"Totakeke\",1427342715000,13\n\"Totakeke\",1427342742000,12\n\"Totakeke\",1427342751000,13\n\"Totakeke\",1427342781000,14\n\"Totakeke\",1427342795000,14\n\"Totakeke\",1427342799000,15\n\"Totakeke\",1427342830000,16\n\"Totakeke\",1427342859000,17\n\"Totakeke\",1427342859000,18\n\"Totakeke\",1427342872000,19\n\"Totakeke\",1427342891000,19\n\"Totakeke\",1427342946000,20\n\"Totakeke\",1427342967000,21\n\"Totakeke\",1427342967000,22\n\"Totakeke\",1427342968000,23\n\"Totakeke\",1427342970000,24\n\"Totakeke\",1427343027000,23\n\"Totakeke\",1427343028000,24\n\"Totakeke\",1427343038000,23\n\"Totakeke\",1427343040000,22\n\"Totakeke\",1427343042000,23\n\"Totakeke\",1427343049000,24\n\"Totakeke\",1427343060000,23\n\"Totakeke\",1427343061000,22\n\"Totakeke\",1427343065000,23\n\"Totakeke\",1427343066000,24\n\"Totakeke\",1427343070000,25\n\"Totakeke\",1427343080000,26\n\"Totakeke\",1427343104000,25\n\"Totakeke\",1427343110000,26\n\"Totakeke\",1427343233000,42\n\"Totakeke\",1427343274000,42\n\"Totakeke\",1427343275000,43\n\"Totakeke\",1427343276000,44\n\"Totakeke\",1427343283000,45\n\"Totakeke\",1427343283000,46\n\"Totakeke\",1427343284000,47\n\"Totakeke\",1427343345000,63\n\"Totakeke\",1427343355000,64\n\"Totakeke\",1427343357000,65\n\"Totakeke\",1427343442000,93"
        },
        {
            "name": ".0/group_by1/arrange2",
            "source": ".0/group_by1/arrange2_flat",
            "transform": [
                {
                    "type": "treefacet",
                    "keys": [
                        "data.Player"
                    ]
                }
            ]
        },
        {
            "name": "scale/stroke",
            "format": {
                "type": "csv",
                "parse": {

                }
            },
            "values": "\"domain\"\n\"Mr. Sabotage\"\n\"Ms. Launch\"\n\"Ms. Production\"\n\"Totakeke\""
        },
        {
            "name": "scale/x",
            "format": {
                "type": "csv",
                "parse": {
                    "domain": "number"
                }
            },
            "values": "\"domain\"\n1427342347900\n1427343494100"
        },
        {
            "name": "scale/y",
            "format": {
                "type": "csv",
                "parse": {
                    "domain": "number"
                }
            },
            "values": "\"domain\"\n-4.65\n97.65"
        }
    ],
    "scales": [
        {
            "name": "stroke",
            "type": "ordinal",
            "domain": {
                "data": "scale/stroke",
                "field": "data.domain"
            },
            "points": true,
            "sort": false,
            "range": "category10"
        },
        {
            "name": "x",
            "domain": {
                "data": "scale/x",
                "field": "data.domain"
            },
            "type": "time",
            "clamp": false,
            "range": "width"
        },
        {
            "name": "y",
            "domain": {
                "data": "scale/y",
                "field": "data.domain"
            },
            "zero": false,
            "nice": false,
            "clamp": false,
            "range": "height"
        }
    ],
    "marks": [
        {
            "type": "group",
            "from": {
                "data": ".0/group_by1/arrange2"
            },
            "marks": [
                {
                    "type": "line",
                    "properties": {
                        "update": {
                            "stroke": {
                                "scale": "stroke",
                                "field": "data.Player"
                            },
                            "x": {
                                "scale": "x",
                                "field": "data.Time"
                            },
                            "y": {
                                "scale": "y",
                                "field": "data.Buildings"
                            }
                        },
                        "ggvis": {
                            "data": {
                                "value": ".0/group_by1/arrange2"
                            }
                        }
                    }
                }
            ]
        }
    ],
    "width": 672,
    "height": 480,
    "legends": [
        {
            "orient": "right",
            "stroke": "stroke",
            "title": "Player"
        }
    ],
    "axes": [
        {
            "type": "x",
            "scale": "x",
            "orient": "bottom",
            "layer": "back",
            "grid": true,
            "title": "Time"
        },
        {
            "type": "y",
            "scale": "y",
            "orient": "left",
            "layer": "back",
            "grid": true,
            "title": "Buildings"
        }
    ],
    "padding": null,
    "ggvis_opts": {
        "keep_aspect": false,
        "resizable": true,
        "padding": {

        },
        "duration": 250,
        "renderer": "svg",
        "hover_duration": 0,
        "width": 672,
        "height": 480
    },
    "handlers": null
}
;
ggvis.getPlot("plot_id986029526").parseSpec(plot_id986029526_spec);
</script><!--/html_preserve-->

With the graph generated, it becomes readily apparent that this graph doesn't convey enough information as well to be useful. The graph doesn't show the types of building that has been constructed at each point so this information needs to be included. Different types of buildings produce different resources and knowing this is key to understanding whether a resource will have more supply than demand so a fourth dimension needs to be added to the graph. The tricky thing about this is that there are a total of twenty different buildings in the game so even adding points and styling them is not a viable solution. 

![Some of the different types of resources and buildings in the game](../assets/justin/images/resources.png)

### Buildings Table
Adding a table to visualize the category of tables is now necessary, but conveying data across time in a table generates too many rows, occupying too much vertical space, and makes it tedious to read through all the information. One solution to this problem is animating the table over time which allows the time component to be removed from the graph and allows the table to be much more easier to read. One of the options available to make interactive charts using R is [Shiny](http://shiny.rstudio.com/) and they do have [animated sliders](http://shiny.rstudio.com/gallery/sliders.html) which appears to meet what is required here. 

![Animated slider... potentially dangerous](../assets/justin/images/timeslider.png)

The smoother the animation is the better but animation tends to be performance intensive so it is prudent to explore the capabilities of the animated slider. The animated slider at each step returns an updated variable and we can use this variable to update their corresponding visualizations. So the main variables to tweak for the animated slider is the step size between each frame and the time interval of each animation. Just by animating the graphs, we can already determine that when the animation interval drops to 200 and below, the animation breaks very early in the chart and freezes everything else in the application. So for this visualization, I will proceed with an interval of 500 and a step size of 0.5.

[Performance testing of animated slider](https://totakeke.shinyapps.io/AnimatedSlider/)

Following that, minimizing computation during animations is also crucial to allow for smoother animation. The building table requires transformation from the original data showing player actions to a table with each column representing the different buildings. So most of the heavier data transformations have been done offline and generated as separate csv files to minimize impact on performance. The first table below represents the original data and the second table represents the transformation. What might be also evident that having a 22 column wide table with the column names being building names would occupy too much horizontal space. 


      Time    Building               Action      Buildings  Player           Message                                   
----  ------  ---------------------  ---------  ----------  ---------------  ------------------------------------------
142   15:45   Ms. Launch             Takeover            0  Ms. Launch                                                 
143   15:45   Ms. Launch             Takeover           63  Totakeke         Totakeke has taken over Ms. Launch        
144   15:55   Electrolysis Reactor   Build              64  Totakeke         Totakeke has built a Electrolysis Reactor 
145   15:57   Electrolysis Reactor   Build              65  Totakeke         Totakeke has built a Electrolysis Reactor 
146   17:22   Ms. Production         Takeover            0  Ms. Production                                             
147   17:22   Ms. Production         Takeover           93  Totakeke         Totakeke has taken over Ms. Production    

      Time    Player            Geothermal.Plant   Solar.Panel   Wind.Turbine   Electrolysis.Reactor   Hydroponic.Farm   Water.Pump
----  ------  ---------------  -----------------  ------------  -------------  ---------------------  ----------------  -----------
145   15:45   Ms. Launch                       0             0              0                      0                 0            0
146   15:45   Totakeke                         0             4              5                      6                 5            6
147   15:55   Totakeke                         0             4              5                      7                 5            6
148   15:57   Totakeke                         0             4              5                      8                 5            6
149   17:22   Ms. Production                   0             0              0                      0                 0            0
150   17:22   Totakeke                         0             7              7                     12                 7           10

In order to prevent the table from going too wide, there are two hacks being employed here. First, the buildings are replaced by icons of the buildings taken from the [wikipedia site](http://offworldtradingcompany.gamepedia.com/). This is actually more tricky than it seems because data frames don't store image data, so the image paths need to be transformed into html output (i.e. <img src"images/Building_geothermal_plant.png />") for Shiny to render. The rendered table needs to be specified so that it outputs raw html and this can be accomplsihed by using the function (sanitize.text.function = function(x) x). The second hack here is to split the columns of the table into two and stack them vertically. This is difficult to accomplish using data frames that have strict data types so the data is transformed into matrices using the rbind function in R. 

![Hacking with matrices and outputting raw html to generate images](../assets/justin/images/matrix_table.png)

To top this off, conditional formatting of the values was also used to highlight which values increased or decreased from the previous interval. Again, there are no built-in functions within Shiny for this so another hack similar to the one used for the images was employed. First, the data was transformed again to indicate which values have increased or decreased at each time interval so the data transformation is tied to the time slider interval value. A combination of HTML div tags and CSS formatting is then used to format the text color and text property at each interval. 

### Message Log

So the graph is almost done but it is missing the granular information of when and what exactly was built. The table doesn't accomplish this as it only updates every interval so every action within an interval cannot be separately identified. One method to address this is to layer points on the graph and use tooltips to display this information to the user. Unfortunately among the available interactive chart packages with tooltips enabled, rCharts proved to be too new and lacks documentation for simple customizations while ggvis bugs out when layer_line is used with tooltips. 

![ggvis layer_lines doesn't play well with tooltips](../assets/justin/images/ggvis_fail.png)

Since the graph issue is difficult to fix and decreasing the step size of the animation was not an option either, I decided to print out the actual actions as text messages while using the time slider value to filter. The first idea was to simply extract the last few messages given the current time indicated by the slider. This solution had issues as not only did it present limited amount of messages, if the amount of messages within the step or time interval were more than the amount of messages displayed, then some of the earlier messages would be lost. So the ideal would be to display all the messages while not taking up too much space... which is what a chat box does using a scroll bar. 

[ShinyChat, hipper than IRC](http://shiny.rstudio.com/gallery/chat-room.html)

Thankfully someone did implement a chat room interface using Shiny so I basically used the same implementation for the message log. The first thing required to make it scrollable is to simply use CSS to specify the size of the region and use the overflow-y property. The second thing that was required was javascript because the chat box by default doesn't scroll to bottom every time it is updated. A javascript function was necessary to force the chat box to scroll to bottom at a specific time interval.

##### CSS Code

```r
#chat {
  padding: .5em;
  border: 1px solid #777;
  height: 150px;
  width: 340px;
  overflow-y: scroll;
  font-size: 12px;
}
```

##### Javscript Code

```r
var oldContent = null;
window.setInterval(function () {
    var elem = document.getElementById('chat');
    if (oldContent != elem.innerHTML) {
        scrollToBottom();
    }
    oldContent = elem.innerHTML;
}, 50);

// Scroll to the bottom of the chat window.
function scrollToBottom() {
    var elem = document.getElementById('chat');
    elem.scrollTop = elem.scrollHeight;
}
```

### Style Formatting

With all that done, most of the remaining work is styling so it looks appropriate. For that purpose, I decided to employ most of the designs and colors of the game so it actually looks like it belongs to the game. Most of the formatting is done with CSS except for ggvis which isn't affected by CSS rules. To change the colors of the lines so they are the same as the colors used in game, another hack is used, which is creating a new column containing the exact color representing each player. Aside from that, most of the remaining styling options in ggvis is can be gleaned around information scattered around the internet. What was the most useful was perhaps reading the [vega documentation](https://github.com/trifacta/vega/wiki/Axes) which ggvis is based on and understanding how the options relate to ggvis options. At the end, more than fifty options were specified to customize the ggvis graph in order to look similar to the graphs within the game.

## Final Visualization

With all that done, I can now present the final visualization to you... in a link. Unfortunately it seems impossible to render Shiny within a HTML page and this places a significant limitation of what Shiny applications can accomplish on the web. Still, the functionality it provides is quite impressive and is worth exploring to see whether it fits your specific needs.  

I am including a static screenshot of the application, the link to the application hosted on the shinyapps website, and the source files.

![Screenshot of the final visualization](../assets/justin/images/final.png)  
[Visualization hosted on shinyapps](https://totakeke.shinyapps.io/Offworld/)  
[Source files](https://raw.githubusercontent.com/Totakeke/edav/gh-pages/assets/justin/offworld.zip)

## Further Improvements

There are a lot of remaining ideas I have for this visualization that could not be implemented due to time and complexity. Here's a number of items that can be still explored.

- Visualizing the message log better. As mentioned, tooltips on points on the graph would be nice, but so far a solution without significant compromise of everything else is still missing.  
- Styling the message log scroll bar. For the current design, the scroll bar on the message box looks a bit out of place. There doesn't seem to be browser standards in place to customize scroll bars but there are numerous jQuery stylized scroll bars that can be used.
- Fixing the scale on the time slider. Technically the x-axis time scale is in minutes and seconds however I have not been able to figure out whether the sliders can use a time scale instead of a simple numeric scale.
- Improving performance of the tables. Rather than refreshing the whole table, we would only want to refresh the values within the tables during animation.
- Changing the way the graph animates. Currently the graph is rather jittery because it is unlike actual animation where there is a new frame on each interval. A better way to accomplish this while improving performance is perhaps something akin to a mask layer over the plots. The mask would move to the right and reveal more of the plot as the time slider moves. This would also solve the issue of the plots seemingly not moving along with the slider. This probably requires javascript and quite difficult to implement on top of ggvis. 
- Adding more data on the same graph. Factors such as distance of building from HQ, number of adjacent buildings, and resources being extracted are still missing from the graph and would provide even more information 
- Adding other graphs using tabs. It would be nice with the time slider as the main control to visualize other sets of data as well including the stock and resource price seen before. 
- Filtering players. The in-game graphs has this capability to select which items to show so it would be nice to have here as well. Showing the building tables in between the checkboxes and players is probably something else that needs to be hacked together.
- Animating the chat box better. Currently the chat box looks a bit unnatural during animation because unlike an actual chat box, messages are not delivered one at a time. 
- Further compressing the building tables. The current layout works upt to 4 players but would take up too much vertical space for 8 players. One option is to lay the values on top of the images on a bottom right corner so instead each player take up four rows, they would only require two.
- Other performance improvements. Rbind has said to be slow so perhaps optimizing each of the transformation functions used can further improve animation and performance. 

This is in essence still a relatively simple chart but each component requires a lot of customization in order to make them function and look appropriate. It was interesting working with Shiny and I hope you enjoyed reading through this post as well. Any feedback is appreciated and it would be great to hear your thoughts. 
