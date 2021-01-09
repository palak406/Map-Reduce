# Map-Reduce

Imagine we are working with a terabyte-scale dataset and we have a MapReduce
application we want to test with that dataset. Running our MapReduce application against
the dataset may take hours, and constantly iterating with code refinements and rerunning
against it isn’t an optimal workflow.

To solve this problem we look into sampling, which is a statistical methodology for extracting
a relevant subset of a population. In the context of MapReduce, sampling provides an
opportunity to work with large datasets without the overhead of having to wait for the
entire dataset to be read and processed.

Designing a map/reduce program that implements a random sampler.

The input test data for this problem is in the cookbook.zip file.
The sampling method is reservoir sampling algorithm
