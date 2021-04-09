<script context="module">
    export let data3 = [];
    import { onMount } from "svelte";

    export async function preload() {
        
        const apiURL = "symbols.json";
        const response3 = await this.fetch(apiURL);
        let dataTemp = [];
        dataTemp =  await response3.json();
        data3 = dataTemp;
        
        console.log(1+1);
        const response = await this.fetch("data.json");
        const responseJson = await response.json();

        const response2 = await this.fetch("symbols.json");
        const responseJson2 = await response2.json();
        return {
            symbols: responseJson2,
        };
    }

    async function fetchSymbolsAndData() {
        const [symbolResponse, dataResponse] = await Promise.all([
            fetch("symbols.json"),
            fetch("data.json"),
        ]);
        const symbols = await symbolResponse.json();
        const data = await dataResponse.json();
   
        return [symbols, data];
    }

    fetchSymbolsAndData()
        .then(([symbols, data]) => {
            symbols; // fetched symbols
            data; // fetched data
            console.log(symbols);
            console.log(data);
        })
        .catch((error) => {
            // /symbols or /data request failed
        });

        
</script>

{#each data3 as item }
<div>
    <p> {item.company} </p>
</div>
{/each}

<script>
    import Listings from "../components/Listings.svelte";
     
    export let symbols;
    
</script>

<svelte:head>
    <title>Listings | Lactuc.at</title>
    <meta name="description" content="Dummy sapper/svelte project - listings" />
    <script
        src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
</svelte:head>

<Listings allSymbols={symbols} />
