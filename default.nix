{ pkgs ? import <nixpkgs> {} }:
with pkgs.python311Packages;
pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.virtualenv
    pkgs.python311Packages.tornado
    pkgs.python311Packages.aiohttp
  ];

  shellHook = ''
    # Create a virtual environment and activate it
    python -m venv venv
    source venv/bin/activate
    pip install openai

    # You can add more setup steps if needed
  '';
}
