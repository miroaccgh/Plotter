{pkgs, ... }:

{
  languages.python.enable = true;
  languages.python.version = "3.3.1";
  enterShell = ''
    python -m venv env
    . env/bin/activate
    python setup.py
  '';
}
