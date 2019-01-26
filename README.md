# DATA_VISUALISATION-Retailer-data

**Study on footwear options**

This report accounts for the relatively high sales of footwear across the two-years period 2017/18. To have a clear idea of the sales it is crucial to focus on the discount every category has been subjected to. GRAPH 1 shows the max-discount averaged per category in the years 2016/17.

<img src="https://github.com/dimaggiofrancesco/DATA_VISUALISATION-Retailer-data/blob/master/Figure_1.png" width="600" height="400" />
  
As shown in the bar chart, the less discounted sectors are: accessories, beauty, non-apparel, and suits-sets. The remaining sectors were subjected to an average discount of approximately 40%. The trend of discounts was very similar across UK and US sales, with a constantly lower discounts applied to UK products. A direct effect of these applied discounts can be appreciated by examining the two graphs below, which show the absolute (GRAPH 2a) and relative (GRAPH 2b) percentage of options that did not sell-out during these two years.

![enter image description here](https://lh3.googleusercontent.com/Em_aeYyKe47HBWxp-3OdHxqY6YzhdtNtshAMyZCgiCy7P3ggVLspHQlgS-Fynb-6g7hkuH5aFVtfVQ)

![enter image description here](https://lh3.googleusercontent.com/rtYq-dvmmJyUYcko8AJM7UHQAr9pWOgoRjG46mnYR2J0jVHirTSpp4aoAvp-p0x_03KTaYBvFYABrg)

It is worth to mention that the categories subjected to a lower discount are those with relatively less sell out. On the contrary, all the other categories showed a relatively high sold out percentage. GRAPH 3 shows the correlation between the percentages of the discount applied versus the percentages of the options that did not see-out for both UK (blue, GBP currency) and US (orange, USD currency) market. The graph exhibits a linear trend where the percentage of the options that did not sell-out decreases with the increased applied discount.

![enter image description here](https://lh3.googleusercontent.com/aP4b8Qx-O2FJ5hEXOdurPHQGfUSc6-dQ2h7NoTO71XN2scTLBys0JFbvmFx97CVeJEgnGQrYaJX5Zg)

In this report I would like to focus on the footwear options, which displayed the highest sales compared to the other categories (GRAPH 2a and 2b), despite their max-discount, 40%, was in line with most of the categories (GRAPH 1). The relatively high sales of footwear could play an important role for the overall income. By increasing the price or by reducing the max-discount, we would expect to have a slightly decrease in sales, but an overall higher income. GRAPH 4a and 4b show the footwear max-discount and price grouped by month.
![enter image description here](https://lh3.googleusercontent.com/iZX1Xi-7PWUi0-Lyg2KXYCmyFJVXycHnL9Qivb3K6totubZSR-M0PQYNBOdjUTgqjv9k6MMJH5PcNQ)
![enter image description here](https://lh3.googleusercontent.com/KKahAXH2VL5PmsxLsRcxwy-8Ko-gGSnCx_QPJcJrtjkYBRqBbxRDVt2i3X3IIPDeDBiHmp-8ifJcSQ)

The graphs exhibit a higher discount percentage for footwear items sold in United States (USD) compared to Great Britain (GBP) market. GRAPH 4b shows an average increase of price from approximately 360 USD in January up to a peak value of approx. 540 USD reached in October, before decreasing again to the value of 360 USD. This price increase resulted in an average increase of 50% of the original value. On the other hand, the GBP prices showed a relatively moderate increase, around 30%, from the lowest value of 275 GBP in January, up to the maximum value of about 350 GBP in August. Considering the results previously discussed in GRAPH 2a and 2b it would be reasonable to level the price in USD to approximately 400 USD in order to have a lower variation across the year and possibly increasing the revenue. A similar result could be obtained by slightly increasing the price in GBP.

The histogram in GRAPH 5 shows the distribution of the days passed from when the footwear stock went live on the website and the day of the options sold out.

![enter image description here](https://lh3.googleusercontent.com/HmIbWtcf22PHKc0AiugcaKec2IV1AGIIeG3LnD7ymZYjk4LKWv_1w1IyvyQb871OkyCKH8mrs3KC_A)

Both UK (GBP) and US (USD) markets display Gaussian trends with USD market having the centre of the peak slightly shifted towards lower x-axis values: 140 days compared to 150 days for UK stocks. These results provide important information on when the stock should be replenished.


**Thinking process**

**GRAPH 1:** When I looked at the data file I wanted to have a picture to have a general idea. I think an easy way to do it is to group the records in a field. ‘Product name’, ‘brand’, ‘description’ have too many records to be grouped by. ‘Category’ has only 14 records so I thought that would be the perfect field. So I grouped the category and currency field and averaged per ‘max_discount’.

In almost all the graphs I decided to separate the 2 markets: UK (GBP) and US (USD). The fields: ‘currency’, ‘market’ and ‘shop’ showed the same information so I decided to just use the currency one. The field ‘in_stock’ did not show any valuable information since all the records were the same.

**GRAPH 2a – 2b:** After looking at the discount graph (GRAPH 1) I decided that it would have been good to work on the sell-out field to have an idea on the sales. Briefly, I wanted to check what was the percentage of options that did not sell-out (in each category). I showed it in 2 graphs, GRAPH 2a shows the absolute percentage of options that did not sell-out (not normalised) whereas GRAPH 2b shows the same results normalised by 100 (100%). The values in GRAPH 2a were used to create GRAPH 3. On the other hand, GRAPH 2b gives a quick and easy to way to visualise the options with low/high sell out (high/low percentage).

**GRAPH 3**: I was thinking that there was a correlation between applied discount (GRAPH 1) and the options that did not sell-out (GRAPH 2a). To investigate this I created this graph and indeed it shows a good correlation between sales (based on sell-out info) and discount.

**GRAPH 4a – 4b:** I decided to choose one category and to obtain detailed information on it. I could have chosen any category. I chose ‘footwear’ because it had the lowest relative percentage in GRAPH2b meaning that the options had the maximum sell-out rate. I thought that by looking at this category more in detail it could have helped to increase the revenues by modifying either the mean discount or the mean price applied to this category. I decided to show the data as a function of the months.

**GRAPH 5:** The last graph is not related to the other 4. I just wanted to check how long it takes for the footwear to be sold-out. I decided to show this information using the histogram style. By knowing this data it could be possible to modify the time for the restocking.
