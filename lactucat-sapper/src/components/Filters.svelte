
<script>
    import symbols from "./Card.svelte";
    import Select from 'svelte-select';
    let selectedTicker = undefined;


</script>

<div id="searchBox">
    <form method="get" action="">
        <div class="tb">
            <div class="td">
                <Select {items2} on:select={handleSelect}></Select>
            </div>
        </div>
    </form>
</div>

{#if selectedTicker}
	<p>Selected symbol is: {selectedTicker.label}</p>
{/if}

{#each data as item }
<div>
    <p> {item.title} </p>
</div>
{/each}

<style>
 	:global(input) {
		margin: 0;
	}
</style>
