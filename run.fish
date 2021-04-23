#!/usr/bin/fish
for i in (seq 0 10)
    wsk action invoke run_application --param-file $argv[1]
end
