# hello_universe
example python assignment with (JMU-CS-style) gradescope autograder

# goal
Assume I'm an instructor who isn't otherwise using Python. Thonny should do it all. 

# current problem
I use the Thonny `Tools` -> `Open system shell...` and run the build script.

It runs! 

The test doesn't work with 
```
{
    "tests": [
        {
            "name": "Check submitted files",
            "score": 0,
            "max_score": 0,
            "output": "All required files submitted!\n"
        },
        {
            "name": "Outputs \"hello\".",
            "score": 0.0,
            "max_score": 8,
            "output": "Test Failed: name 'to_lower' is not defined\n"
        }
    ],
    "leaderboard": [],
    "visibility": "visible",
    "execution_time": "0.00",
    "score": 0.0
}
```

what weird thing did i do that makes the to_lower be not defined?