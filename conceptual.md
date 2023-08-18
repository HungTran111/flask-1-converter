### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Syntaxs, python have esay code readabality and maintain code.
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1st method: get()
  2nd method: setdefault()

- What is a unit test?
  a way of testing unit

- What is an integration test?
  a type of software testing in which the different units

- What is the role of web application framework, like Flask?
  let you develope aplication easier

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  (like '/foods/pretzel') predefined and (like
  'foods?type=pretzel') for search based routing

- How do you collect data from a URL placeholder parameter using Flask?
  you can specify the variable in the app.route and then use that variable as a paramater in the routing function.

- How do you collect data from the query string using Flask?
  can be found in the request.args


- How do you collect data from the body of the request using Flask?
  can be found in the request.args

- What is a cookie and what kinds of things are they commonly used for?
  a cookie is information that a website puts on a user's computer. 

- What is the session object in Flask?
  use to set and get session

- What does Flask's `jsonify()` do?
  return a response object
  