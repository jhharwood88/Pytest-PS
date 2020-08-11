
def fizzbuzz(n, additional_rules=None):
    """
    Convert a number to it's name in the game FizzBuzz
    >>> fizzbuzz(2)
    '2'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(7, {7: "Whizz"})
    'Whizz'
    >>> fizzbuzz(35, {7: "Whizz"})
    'BuzzWhizz'
    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer

#This makes use of the docstirng to pass test results to the player, but with the aditional rules it lets the player know by making use of the dummy information. For the most park, dummies are none or empty values. Dummys can arguably not be considered test objects as they have no value, but are used when forced to pass an arguemnt to the test.