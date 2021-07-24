package main

import (
	"flag"
	"log"

	"github.com/BurntSushi/toml"
	"github.com/ivan339339/archiviste/internal/app/apiserver"
)

var (
	configPath string
)

// Инициализация апи с параметрами запуска
func init() {
	flag.StringVar(&configPath, "config-path", "configs/apiserver.toml", "path to config file")
}

func main() {
	flag.Parse()

	congif := apiserver.NewConfig()
	_, err := toml.DecodeFile(configPath, congif)
	if err != nil {
		log.Fatal(err)
	}

	s := apiserver.New(congif)
	if err := s.Start(); err != nil {
		log.Fatal(err)
	}

}
