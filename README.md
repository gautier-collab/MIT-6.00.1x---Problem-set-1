# MIT-6.00.1x-Problem-set-1


Those are my containerized programs solving the first problem set of the course "Introduction to Computer Science and Programming Using Python" (MIT 6.00.1x) of the Massachusetts Institute of Technology.



Problem 1:
That program counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. s must be a string of lower case characters.

Problem 2:
That program prints the number of times the string 'bob' occurs in s. s must be a string of lower case characters.

Problem 3:
That program prints the longest substring of s in which the letters occur in alphabetical order. In the case of ties, it prints the first substring. s must be a string of lower case characters.



To execute each of these programs, open the corresponding problem repository in your UNIX terminal and run the following line:
sudo docker build -t mit-python-problem-1 . && echo -e "\n\n" && sudo docker run -i -t mit-python-problem-1
