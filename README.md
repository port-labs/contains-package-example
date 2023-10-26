# Ingesting Requirements.txt Dependencies


## Getting started

In this example, you will create a blueprint for `package` entity that ingests all third party dependencies in your requirements.txt file using Port's GitOps functionality. You will then create a calculation property (`contains`) on this blueprint to check whether a specific package is present in the content of the file. Finally, you will add the `port.yml` file in your project's root folder to enable Port to read and parse the requirements.txt file. In this example, delete the row "nugpak" row from the port.yml.

## Package Blueprint
Create the service blueprint in Port [using this json file](./resources/blueprint.json)

### Calculation Property
The provided example in the `blueprint.json` uses the `jq` mapping to check if the `content` of the blueprint entity contains the `requests` library. Please change `requests` on line 20 to match your specification.

### Package Entity Created
![Package Entity Created](./assets/package.PNG "Package Entity Created")


# Ingesting  Package.nuspec Dependencies
NuGet package file is XML based, so we will ingest it into a String property, and make calculations on that property to check whether our project uses specific dependencies.
After that, you will add port.yml to your repository's root folder, for Port to be able to read and parse the package.nuspec file. In this example, delete the row "content" from the port.yml

## Getting started
In this example, you will create a blueprint for `package` entity that ingest all data from your NuGet file into a String property.

## Package Blueprint
Create the service blueprint in Port [using this json file](./resources/nugBlueprint.json)

### Calculation Property
The provided example in the `nugBlueprint.json` uses jq mapping to check if the `nugpak` string property contains a specific package. In this example, the string being searched is `TestPackage` as noted in line 21 of the Blueprint JSON. Change the package name to the desired one, Caps sensitive.