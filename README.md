
## Problem 1: 

> Using the language of your choice, write a function that validates a JSON string is
> formatted correctly. The function should return a simple Boolean indicating true if the string is
> correct and false if there is any problem with it.
> The function should use these assumptions regarding the JSON string:
> • A JSON object is encapsulated in {} curly braces and includes a comma-separated list of
> key-value pairs
> • A JSON array is encapsulated in [] square braces and includes a comma-separated list of
> values
> • A key-value pair is in the format of “key”:value where key is always a quoted string and
> value is either a quoted string, a number, a nested JSON object, or a nested JSON array
> An example of valid JSON would be:
> { “key1” : “value1”, “key2” : [“value2”, “value3”], “key3” : { “subkey1” : 123 } }
> As we are not parsing the string, any whitespace and the content of the keys/values should be
> ignored. The function should only be checking the order of symbols.
> 

Unfortunately I was not able to understand fully the ask. Points of confusion 
was the phrase:

> The function should use these assumptions regarding the JSON string: ...

I do not know what it means for a function to 'use' an assumption.
Does it mean I need to validate these assumptions?
If so why the following phrase:

> As we are not parsing the string, any whitespace and the content of the keys/values should be
> ignored. The function should only be checking the order of symbols.

How does a function whose job is to validate can both use an assumption and ignore
the content of key/values?

Also importantly the word 'symbols' was not defined

Nonetheless, I have a very simplistic program and its accompaying unit tests:

> https://github.com/L271828R/broadridge/blob/main/problem_1/json_parser_simple.py
> https://github.com/L271828R/broadridge/blob/main/problem_1/test_json_simple.py

for the above 'symbols' only mean: "[", "]", "{", "}"

For the above I showcase the basic workings of a stack object as would be asked
from a beginner level 'HackerRank' or "Leetcode' testing challange.


Additionally, I have a more complete solution where:

* Proper JSON rules are followed and the content of both dictionaries and lists are validated.
* JSON needs to start with "{" and finish with "}" 
* Here symbols mean: "[", "]", "{", "}", ":", ","
* Incorrectly formatted JSON such as '{"key"::"value"}' will return false

> https://github.com/L271828R/broadridge/blob/main/problem_1/json_parser.py
> https://github.com/L271828R/broadridge/blob/main/problem_1/test_json.py

I hope somewhere between the two examples I provided I was able to fulfull the requirement.
Thank you.

## Problem 2: 

> We are testing the payment processor for a vending machine. The typical flow of a
> vending machine purchase is: user inserts bills and coins, user selects an item to purchase, the
> payment processor validates the inserted money is sufficient, and returns change if money
> inserted is greater than the cost.
> Using the testing framework/language of your choice, write test cases to verify the function
> that checks the money inserted is sufficient to purchase the requested item. The function
> signature is (in Java):
> public boolean validatePurchase(Integer itemId, BigDecimal money);
> You can assume you have access to two functions to get item information:
> public List<Integer> getItemIds(); // returns all item IDs
> public BigDecimal getPriceForItem(Integer itemId); // returns price for an item
> You should assume that the function will throw an exception in any situation where the
> function cannot process the input.
> 

Kindly see the following test:

> https://github.com/L271828R/broadridge/blob/main/problem_2/vending_machine.py
> https://github.com/L271828R/broadridge/blob/main/problem_2/test_vendingmachine.py

## Problem 3:

> We are testing a service product that allows two ways for customers to interact with
> it: through a web UI or through a public REST interface. We are using two different testing
> frameworks, one for each form of interaction, and we want each of them to have access to the
> underlying databases and dependencies the product uses so that we can verify the data coming
> from the product.
> For the purposes of this example, the product in question relies on data from three different
> databases. One contains user data, one contains company data, and one contains data of
> activity done through the product. The product also makes calls to two external services owned
> by other teams through REST, one is a single sign-on server that handles authentication for the
> product, and the other provides market data that the product displays along with its own data.
> How do you design your project so that both the UI testing framework and REST testing
> framework do not have to write their code for interacting with those databases and external
> systems? No code is required for this answer, but be specific about where the code would live
> and how the frameworks would use that code.

* Requirement 1: "we want each of them to have access to the underlying databases and dependencies the product uses so that we can verify the data coming from product"
* Requirement 2: "how do you design your project framework so that you do not have to interact with those databases and external systems?

>
> Database dependencies: [ [user_data_db], [company_data_db], [activity_db] ] 
> 
> REST service dependencies: [sso service REST], [market data REST] ] 
> 

## Database problem

For not calling on the actual database dependencies I would mock/stub the objects
that call the database have objects return deterministic data. 

For example:

> db = Mock(DataBase("user","password","connectionstring")) // Mocking the object
>
> db.result_set = ["user1", "user2", "..."]  // stubbing the data with expected results
>
> productService = ProductService()
>
> productService.get_userdata(db) // passing mocked/stubbed object via injection
    
Where does this live?:
Code mocking would like inside the test framework as a utility module.

Addition info:

https://circleci.com/blog/how-to-test-software-part-i-mocking-stubbing-and-contract-testing/


## Service Problem

For not calling on the actual restful services, I would implement a ip:port stubbing
service like "wiremock". In essence it is process that lives next to the main process
you are testing and it listens for a certain IP:port (ie: 192.168.1.67:3000/get_sso&user=user1 )

The wireock service would listen for certain REST verbs and endpoints and return
deterministic data.

Where does this live?:
The wiremock service would be a deamon or a background process as part of the OS that hosts
the testing suite.

Additional info:

http://wiremock.org/


