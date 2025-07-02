# Coding Standards

## General

### Class, Method, Function, and Variable Names
- Intuitive
- Lower case
- Words separated with an underscore
- Do not abbreviate words unless the name becomes excessively long
- Indentation: use tabs instead of spaces
- Recommended to code with an editor showing invisible characters to prevent trailing spaces and tabs

## Applications

Apps are stored in the `fusionpbx/app` directory.

### root.php
- Ensures the `document_root` server variable is set and then sets the include path from the root of the website.

### app_config.php

#### Application
- `app_name`
- `app_uuid`
- `app_category`
- `app_subcategory`
- `app_description`

#### Menu
- Defines location in the menu.

#### Permissions
- Defines the permissions the application uses and the default groups assigned to those permissions.

#### Data Schema
- Defines the structure of the field names and types.

### app_defaults.php
- Runs during the install and when the upgrade schema is called.

### app_languages.php
- Defines a PHP array of the words, phrases, and sentences used in the project.

### Files
- **Names**
  - Written in lower case
  - Words are separated by an underscore
  - Use full words when possible
  - Do not prefix with `v_` (files currently prefixed this way will be renamed to remove the `v_`)
  - Use a program showing invisible spaces
  - Eliminate tabs and spaces at the end of a line
  - Use line feed only (no carriage return and line feed)

## Database

### Tables
- Prefixed with `v_` (this may be configurable in the future)
- Table names are plural unless the name is an acronym
- Use full words, not abbreviations
- UUIDs used for relational IDs instead of auto-increment identifiers

### Fields
- `domain_uuid`
- Primary key name is the non-plural name of the table without the `v_` prefix
  - **How to create the primary key name**:
    - For a table named `v_users`, remove the `v_`, make it non-plural, and add `_uuid` to the end of the field name. In this example, the primary key would be `user_uuid`.

## Code Documentation
[http://www.phpdoc.org/](http://www.phpdoc.org/)
