<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Duplicate Element Finder</title>

</head>
<body>

<h1>Duplicate Element Finder</h1>

<p>This Python script identifies elements in a given list that appear <strong>exactly twice</strong> and prints them. The script ensures that elements are not printed more than once.</p>

<h2>How It Works</h2>

<p>The script uses the <code>count()</code> function to determine the frequency of each element in the list. If an element appears exactly twice, it is printed. To avoid printing duplicate elements, a set is used to track elements that have already been printed.</p>

<h3>Code</h3>

<pre>
<code>
arr = [10, 20, 40, 30, 50, 20, 10, 20]

# Create a set to track printed elements
printed = set()

# Loop through the list
for i in range(len(arr)):
    # Check if the element appears exactly twice and is not already printed
    if arr.count(arr[i]) == 2 and arr[i] not in printed:
        print(arr[i])
        printed.add(arr[i])
</code>
</pre>

<h3>Example</h3>

<p>For the input list:</p>

<pre>
<code>
arr = [10, 20, 40, 30, 50, 20, 10, 20]
</code>
</pre>

<p>The output will be:</p>

<pre>
<code>
10
20
</code>
</pre>

<h3>Features</h3>

<ul>
    <li><strong>Simple and easy to use</strong>: Just modify the <code>arr</code> variable to check for duplicates in any list.</li>
    <li><strong>Prevents duplicates</strong>: Ensures that each duplicate is printed only once.</li>
</ul>

<h3>Usage</h3>

<ol>
    <li>Copy the provided code into a Python file (e.g., <code>duplicate_finder.py</code>).</li>
    <li>Modify the <code>arr</code> variable with your list of numbers.</li>
    <li>Run the script:</li>
</ol>

<pre>
<code>
python duplicate_finder.py
</code>
</pre>

<p>The script will print elements that appear exactly twice in the list.</p>

<h1>Created by gaurav<h1/>
</body>
</html>
