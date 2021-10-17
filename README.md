
DOING >>>> 

Problem 1: Using the language of your choice, write a function that validates a JSON string is
formatted correctly. The function should return a simple Boolean indicating true if the string is
correct and false if there is any problem with it.
The function should use these assumptions regarding the JSON string:
• A JSON object is encapsulated in {} curly braces and includes a comma-separated list of
key-value pairs
• A JSON array is encapsulated in [] square braces and includes a comma-separated list of
values
• A key-value pair is in the format of “key”:value where key is always a quoted string and
value is either a quoted string, a number, a nested JSON object, or a nested JSON array
An example of valid JSON would be:
{ “key1” : “value1”, “key2” : [“value2”, “value3”], “key3” : { “subkey1” : 123 } }
As we are not parsing the string, any whitespace and the content of the keys/values should be
ignored. The function should only be checking the order of symbols.

step1: ignore or stripout text and empty spaces

validate { }
validate [ ]
validate { "" : "" }
validate [ "", "" ]

step 2: validate { }, [ ]

step 3: validate { "" : "" } // flag inside curly

step 4: validate [ "", "" ] // flag inside brackets




Problem 2: We are testing the payment processor for a vending machine. The typical flow of a
vending machine purchase is: user inserts bills and coins, user selects an item to purchase, the
payment processor validates the inserted money is sufficient, and returns change if money
inserted is greater than the cost.
Using the testing framework/language of your choice, write test cases to verify the function
that checks the money inserted is sufficient to purchase the requested item. The function
signature is (in Java):
public boolean validatePurchase(Integer itemId, BigDecimal money);
You can assume you have access to two functions to get item information:
public List<Integer> getItemIds(); // returns all item IDs
public BigDecimal getPriceForItem(Integer itemId); // returns price for an item
You should assume that the function will throw an exception in any situation where the
function cannot process the input.

Problem 3: We are testing a service product that allows two ways for customers to interact with
it: through a web UI or through a public REST interface. We are using two different testing
frameworks, one for each form of interaction, and we want each of them to have access to the
underlying databases and dependencies the product uses so that we can verify the data coming
from the product.
For the purposes of this example, the product in question relies on data from three different
databases. One contains user data, one contains company data, and one contains data of
activity done through the product. The product also makes calls to two external services owned
by other teams through REST, one is a single sign-on server that handles authentication for the
product, and the other provides market data that the product displays along with its own data.
How do you design your project so that both the UI testing framework and REST testing
framework do not have to write their code for interacting with those databases and external
systems? No code is required for this answer, but be specific about where the code would live
and how the frameworks would use that code.
