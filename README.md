# lactucat

Scripts and web for lactuc.at.

## Scripts


## Svelte/Sapper

### Installation

Running `python setup.py install` should handle installation of the required packages
though if you have pip you can also run `pip install .` (which uses the same backend).

We reccomend you create a virtual environment with miniconda or pyenv or virtualenv
to install the required packages.

### Running the project

Once you have created the project, install dependencies and run the project in development mode:

```bash
git pull https://github.com/rhovious/lactucat
cd lactucat-sapper
npm install # or yarn
npm run dev
```

This will start the development server on [localhost:3000](http://localhost:3000).

# Message to Devs
Hey fellow devs,
Have a look at our handy project here. If you think something sounds up your alley or
have some specific contribution you think could be useful maybe open an issue so we can
register you as an asignee and let everyone know what we're all working on.

Right now top priority is data harvesting and organizing. Once we have an okay data 
bank or at least one thats fetchable we can start really working. 

I don't have any bright ideas on data storage but I think @rhovious has a static ip
we could probably setup with an sftp port. I think my lab has one we can use too but
since it's a professional comp I'd feel less good about that.

Then onto preprocessing algorithms (auto and cross correlations)

Then clustering using an unsupervised learning model

Then onto nonlinear neural network. I have some ideas about making this kinda fancy
as far as using some special activation functions for each node and I can keep the 
matrix of coefficients as a block if I just 0 out the weights and biases for the nodes
so our training time for the non linear network would be the exact same for a regular
ff convolutional NN. I also want branches to reflect actual things rather than like in
regular NN's that just let the machine correlate garbage. Like have the first columns of 
the first three rows be dedicated to correlation between twitter sentiment and volume 
or something (as an example).

### Project organization

The vision is to link up to some fancy looking webpage so it will spit out graphs real
time for devs + friends (maybe open access but I'm initially against that.)

The backend is run by some NN that will be built, ideally it will pull tickers,
feed in the appropriate data and spit out an answer.

This is done by building a data class object which holds all the data of a stock,
running whatever preprocessing it needs and then feeding that to the nn.

The clustering class will be used for making connections between types of data that will 
eventually be used to give us better ideas about how to structure the NN.

The last class is the NN class which will just load in the right coefficients.

NLP will probably be outsourced but then have the data pulled in. I'd like to incorporate
sentiment analysis on SEC filings as a metric into the NN.


More Immediate TODO List:
1. Establish a base of financial data. Preferably with some level of compression-
hdf5 looks like its going to be our friend. It can get to compression ratios of around
1.6:1 which is pretty nice as it goes, look at its docs.

2. Write preprocessing tools 

...


# final ps
theres more info about ideas and stuff to do in each readme in the folders!
