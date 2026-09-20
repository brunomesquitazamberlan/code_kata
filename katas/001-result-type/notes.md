# Notes - Kata #001 Result Type

## Before Coding

* Result[T, E] comes from Rust in order to express:
- OK [T]
- Err [E]

* I could express it like a Protocol

## During Coding

* I used Protocol lib and trying to express it as CustomizedResult. It was my first thought. Then I added two methods is_ok() and unwrap()
* After consulting documentation of how to use Protocol, I decided to create two functions as the instruction mentioned:
Ok()
Err()
* After reading README.md, consulting online documentation my intuition says that i need to connect the concepts but honestly I don't know How

## After First Attempt
* Split the definition of the Protocol as a way to achieve type safety between the definition of the class if self
* Instead of approaching this problem like a functional challenge, I'm going to think it like Object Oriented approach
* The aim of using Protocols is to avoid things like class Ok(CustomizedResult). Its a way of static typing of the duck typing
* Ok class always return True with the method is_ok
* I can define the Protocol with minimum information just passing the proper format and using pass
* I choose to think in Ok and Err like a Generic Type, so both have self.value
* I thought that the Err could return None using unwrap method, but it can mask some problems. So maybe the correct approach is to raise an Exception
* After shipping this solution to run, I wrote the tests with pytest
* The last part was to understand the types Result[T, E]. I started defining T and E as typeVar
