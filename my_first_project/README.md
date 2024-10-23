## What is the model in MVT (Model, View, Template)? The model is the data part:

- It stores and processes the data.
- It contains the business logic, like a calculator that adds 2 plus 2.

## What is the view in MVT? The view acts as a connector:

It accesses and directs the data.
- It controls the flow of requests and responses.
- It checks permissions and performs necessary verifications.

## What is the template in MVT? The template handles the graphical part:

It uses HTML and CSS to display the data.
- For example, it shows a list of shoes stored in the model.

## How do model, view, and template interact? The data flow is as follows:

- The model sends data to the view in an array.
- The view sends that data to the template in a context.
- The template displays the graphical data.

## In reverse:

- A user searches in the template.
- The view receives the search and queries the model.
- The model returns the results to the view.
- The view sends the data to the template for display.

## Note: There should be no direct connection between the template and the model. Always use the view to ensure checks and permissions.
