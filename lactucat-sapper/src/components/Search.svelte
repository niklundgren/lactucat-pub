<script>
    import Card from './Card.svelte';
    import Filters from './Filters.svelte';

    export let todos;

</script>

<Filters />
<ul>
    {#each todos as todo}
        <Card symbols={ todo } />
    {/each}


</ul>
