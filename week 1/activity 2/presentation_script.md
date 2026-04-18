# Housing Prices Dataset - 3 Minute Presentation Script

## Slide 1 - The question behind the dataset
This dataset contains 545 houses and 13 columns. The main question is simple: why are some houses much more expensive than others? The median price is 4.34 million, while the average is 4.77 million. Because the average is higher than the median, the dataset has some expensive houses pulling the average upward.

## Slide 2 - The market has a middle and a high-end tail
Most houses are grouped around the middle price range. The histogram shows many homes between about 3 million and 6 million. A smaller number of high-priced houses sit above that range, reaching up to 13.30 million. This tells us the story is not only about the average price. We also need to understand what separates the high-end homes.

## Slide 3 - Size is the clearest starting point
The clearest numeric relationship is area. When the houses are split into four area groups, the average price rises from 3.54 million in the smallest group to 6.22 million in the largest group. This suggests that bigger homes are usually valued higher, and area should be one of the first variables to consider in any deeper analysis.

## Slide 4 - Features add another layer of value
Size is not the only part of the story. Houses with air conditioning, main road access, a preferred area, or a guest room have higher average prices than houses without those features. Air conditioning has the biggest simple difference, about 1.82 million. Main road access and preferred area are also strong. These are descriptive differences, so they show patterns, not guaranteed causes.

## Slide 5 - Initial story and next step
The initial story is that housing price is shaped by three ideas: space, comfort, and location access. Larger houses tend to cost more. Comfort features make a house more attractive. Location features such as main road access and preferred area also lift the average price. The next step would be to build a regression model to test these drivers together and check which features still matter when the others are included.
