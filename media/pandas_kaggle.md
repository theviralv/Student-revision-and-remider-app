# Summary Functions and maps

**<u>Summary functions</u>** are quiet usable when we want to see data in a restructured different way to cater our needs.

1. `reviews.points.describe()` = describes the data into some simple parameters line count mean etc.
2. `reviews.points.mean()` = prints out the mean value of the column.
3. `reviews.points.unique()` = prints out list of unique elements of the column or series.
4. `reviews.points.value_counts()` = prints unique entries with respective occurrence counts.

**<u>Maps</u>** are used to create new data representations from existing data that present the same data in a different way.

1. `review_points_mean = reviews.points.mean()`

   `review.points.map(lambda p : p  - review_points_mean)`

   This map func. modifies the points column re-mean all the scores to 0. so map takes a series passes each of its individual elements to the function which returns a vale these return vales are compiled as a series which is the return vale of the function.

**<u>Apply</u>** is the equivalent method when we want to transform the whole dataframe. It passes each row (or a column) one by one to the function which returns a value now the return type of apply is based on the return type of the function it may be a series or a dataframe.

```python
def remean_points(row):
	row.points = row.points - review_points_mean
    return row
reviews.apply(remean_points, axis = 'columns')
```

The code above shows use of apply . We call apply from a dataframe with a custom function to apply the changes if the axis is **'columns'** than the custom functions runs for **each row** one by one, but when axis is **'index'** than the function runs for **each column** at a time. Then the apply function returns the changed dataframe to be stored.

**<u>One line mapping</u>** can be done in pandas i.e. without using map or apply we can map manipulated existing data to a new data. It also has to be stored into new series.

1. `review_points_mean = reviews.points.mean()`

   `review.points - review_points_mean`

   This does the re-meaning to 0 in one line.

2. `reviews.country + " - " + reviews.region_1`

   This merges two columns in one line.

3. ||ly we can use <, > , == etc in these one liners.

**<u>From Exercise:</u>**

1. `series_name.idxmax()` = It returns the index of the maximum value in the series.
2. `series_name.max()` = It returns the maximum value in the series.