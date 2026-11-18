package main

import (
	"database/sql"
	"net/http"
	"os/exec"
)

func handler(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		name := r.URL.Query().Get("name")
		rows, _ := db.Query("SELECT * FROM users WHERE name = '" + name + "'")
		_ = rows
		out, _ := exec.Command("sh", "-c", "ping "+r.URL.Query().Get("host")).Output()
		w.Write(out)
	}
}

func main() {}
