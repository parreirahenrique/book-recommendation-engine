# Book Recommendation Engine using KNN
In this challenge, you will create a book recommendation algorithm using K-Nearest Neighbors.

You will use the Book-Crossings dataset. This dataset contains 1.1 million ratings (scale of 1-10) of 270,000 books by 90,000 users.

After importing and cleaning the data, use NearestNeighbors from sklearn.neighbors to develop a model that shows books that are similar to a given book. The Nearest Neighbors algorithm measures the distance to determine the “closeness” of instances.

Create a function named get_recommends that takes a book title (from the dataset) as an argument and returns a list of 5 similar books with their distances from the book argument.

This code:

> get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")

should return:

> [
> &nbsp;&nbsp;&nbsp;&nbsp;  'The Queen of the Damned (Vampire Chronicles (Paperback))', /
> &nbsp;&nbsp;&nbsp;&nbsp;  [ /
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ['Catch 22', 0.793983519077301],  /
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ['The Witching Hour (Lives of the Mayfair Witches)', 0.7448656558990479],  /
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ['Interview with the Vampire', 0.7345068454742432], /
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376338362693787], /
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178412199020386] /
> &nbsp;&nbsp;&nbsp;&nbsp;  ] /
> ]

Notice that the data returned from get_recommends() is a list. The first element in the list is the book title passed into the function. The second element in the list is a list of five more lists. Each of the five lists contains a recommended book and the distance from the recommended book to the book passed into the function.

If you graph the dataset (optional), you will notice that most books are not rated frequently. To ensure statistical significance, remove from the dataset users with less than 200 ratings and books with less than 100 ratings.

The first three cells import libraries you may need and the data to use. The final cell is for testing. Write all your code in between those cells.

