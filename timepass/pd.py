import pandas as pd
fruits = pd.DataFrame(
    {
        "name":["Apple","Banana","Orange"],
        "Store":["Hypermart","Walmart","Supermarket"],
        "cost/kg":[200,50,85],
    }
)
print(fruits)