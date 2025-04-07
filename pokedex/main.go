package main

import (
    "time"

    "github.com/Aetheros9/pokedexcli/internal/pokeapi"
)

func main() {
    pokeClient := pokeapi.NewClient(5*time.Second, 5*time.Minute)
    cfg := &config{
        caughtPokemon: map[string]pokeapi.Pokemon{},
        pokeapiClient: pokeClient,
    }

    startRepl(cfg)
}
