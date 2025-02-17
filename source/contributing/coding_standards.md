# Coding Standards

## **General**

class, method, function and variable names

-   intuitive
-   lower case
-   words separated with an underscore
-   do not abbreviate the words unless it makes the name excessively
    long.
-   indentation use tabs instead of spaces
-   recommended to code with editor showing invisible characters to
    prevent trailing spaces and tabs.

## **Applications**

Apps are stored in fusionpbx/app directory.

**root.php**

-   Ensures the document[root]{#root} server variable is set and then
    sets the include path from the root of the website.

**app_config.php**

**application**

-   app[name]{#name}
-   app[uuid]{#uuid}
-   app[category]{#category}
-   app[subcategory]{#subcategory}
-   app[description]{#description}

**Menu**

-   defines location in the menu.

**Permissions**

-   Defines the permissions the application uses and the default groups
    assigned to those permissions.

**Data Schema**

-   Define the structure of the field names, and types.

**app_defaults.php**

-   Is run during the install and when upgrade schema is called.

**app_languages.php**

-   Defines a php array of the words, phrases and sentences used in the
    project.

**Files**

-   Names
    -   Written in lower case.
    -   Words are seperated by an underscore.
    -   Use full words when possible.
    -   Do not prefix with \'[v]()\' files that are currently prefix in
        this way will be renamed to remove the \'[v]()\'.
    -   Program showing invisible spaces.
    -   To eliminate tabs and spaces at the end of a line.
    -   Line feed only.
    -   No carriage return and line feed.

**Database**

-   tables
    -   Prefixed with [v]() this may be configurable in the future.
    -   Tables names are plural unless the name is used is an Acronym.
    -   Use full words not abbreviations.
    -   uuids used for relational id instead of auto increment
        identifiers.
-   fields
    -   domain[uuid]{#uuid}
    -   Primary key name is the non plural name of table without the
        [v]() prefix.
        -   How to create the primary key name
        -   If the table name is v[users]{#users} take remove the
            \'[v]()\', make it non-plural and add \'[uuid]{#uuid}\' to
            the end of the field name. In this example the primary key
            would be user[uuid]{#uuid}

Code Documentation

<http://www.phpdoc.org/>
