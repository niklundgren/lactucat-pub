<script>
    import Card from './Card.svelte';
    import Filters from './Filters.svelte';
    import Select from 'svelte-select';
    import loadOptions from './symbols.js';
    import SearchItem from './StockSearchItem.svelte';
    
    let selectedTicker = undefined; //from the web API request

    export let allSymbols; //from the JSON data file
    export let allData;
    export let readData;


    function handleSelect(event) {
		selectedTicker = event.detail;
	}

    const optionIdentifier = 'symbol';
    const getOptionLabel = (option) => option.symbol;
    const getSelectionLabel = (option) => option.description;
    console.log("in listings")
    console.log((option) => option.description);
    
</script>

<Select {loadOptions} {optionIdentifier} {getSelectionLabel} {getOptionLabel} {SearchItem} on:select={handleSelect}  placeholder="Search for Stocks"></Select>

<span class="row">
    <span class="column">
{#if selectedTicker}
	<p>Selected Symbol is {selectedTicker.symbol}</p>
{/if}

</span>
<span class="column">
{#if selectedTicker}
	<p>Company is {selectedTicker.description}</p>
{/if}
</span>
</span>


<style>
    :global(input) {
       margin: 0;
   }

    li {
        align-items: flex-start;
        display: flex;
        margin-bottom: .5rem;
        line-height: 1.2;
        justify-content: center;
    }

    .status {
        margin-right: 10px;
    }

    .title {
        width: 300px;
    }

    .completed {
        color: #666;
        text-decoration: line-through;
    }

</style>

