# Project context

While running clinical trials, it is very important for us to understand at which stage of the trial we are in.
Different events in the world might affect the progress, and we need to be able to react to these changes in a
responsible way.

The information about what state a trial is in is spread among different systems. To make sure that we can respond
to a crisis situations, we need to be able to aggregate this information in a single place, and be able to
make it findable for the clinical trial managers.

# Challenges

* The consequences of the above are not yet well understood
* The design of the system is not yet clear. We need to explore possibilities and come up with initial architectural
  proposal that can be evolved later
* To understand technical possibilities with the data homogenisation, we have created a small pipeline that explores
  some ways of solving it.

# Initial questions to explore

1. how might we make the data accessible to the clinical trial managers at the right time in the right place?
2. how might we design the initial data accessibility?
3. is the data homogenisation possible to achieve?
4. any other unknowns that we haven't thought of?

# Setup and Dependencies

## The automated way

The project, and its dependencies, can be set up using [`mise`](https://mise.jdx.dev/)

## The manual way

You need to have the following installed and available in your path:

* python (version 3.10)
* poetry (pip install poetry)

## Dependencies and Running the tests

To install the project dependencies initially, run `poetry install` in the root of the project.

To run the tests, `poetry run pytest` in the root of the project.