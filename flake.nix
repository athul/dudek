{
  description = "Docker Deployer";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, poetry2nix }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
      inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication;
      app = mkPoetryApplication {
        projectDir = ./.;
        preferWheels = true;
      };
    in
    {
      packages.default = app;
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = [
          pkgs.bashInteractive
          pkgs.poetry
          pkgs.python3
        ];
        shellHook = ''
          echo "Initializing Python env"
          poetry shell
        '';
      };
    };
}
