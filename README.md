Using the data provided, build a Flask API that provides the following endpoints:

`/restaurants/near/:lat/:lon`
that returns the 10 or less closest restaurants (max distance 10km)

`/restaurants/near/:address`
that does a geo lookup using nominatim API and return the 10 or less closest restaurants (max distance 10km)

`/restaurants/combo/:cuisine_a/:cuisine_b`
Looking at the data provided, a lot of restaurants include the tag `"cuisine": "italian"`, `"cuisine": "vietnamese"` etc.
Given two distinct cuisines, find and return pairs of restaurants (maximum 10 pairs) that are close to each other.
Think of it like this: You and your friend want to get some food to take away but you want different food than your friend. So you want to find places that are close to each other that provide both cuisines respectively, or both in one place.
