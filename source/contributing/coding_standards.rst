****************
Coding Standards
****************

**General**
------------

class, method, function and variable names

* intuitive
* lower case
* words separated with an underscore
* do not abbreviate the words unless it makes the name excessively long.
* indentation use tabs instead of spaces
* recommended to code with editor showing invisible characters to prevent trailing spaces and tabs.

**Applications**
-----------------

Apps are stored in fusionpbx/app directory.

**root.php**

* Ensures the document_root server variable is set and then sets the include path from the root of the website.

**app_config.php**

**application**

* app_name
* app_uuid
* app_category
* app_subcategory
* app_description

**Menu**

* defines location in the menu.

**Permissions**

* Defines the permissions the application uses and the default groups assigned to those permissions.
 
**Data Schema**

* Define the structure of the field names, and types.

**app_defaults.php**

* Is run during the install and when upgrade schema is called.

**app_languages.php**

* Defines a php array of the words, phrases and sentences used in the project.

**Files**
  
* Names

  * Written in lower case.
  * Words are seperated by an underscore.
  * Use full words when possible.
  * Do not prefix with 'v_' files that are currently prefix in this way will be renamed to remove the 'v_'.
  * Program showing invisible spaces.
  * To eliminate tabs and spaces at the end of a line.
  * Line feed only.
  * No carriage return and line feed.

**Database**

* tables
  
  *  Prefixed with v_ this may be configurable in the future.
  *  Tables names are plural unless the name is used is an Acronym.
  *  Use full words not abbreviations.
  *  uuids used for relational id instead of auto increment identifiers.
   
* fields
  
  * domain_uuid
  * Primary key name is the non plural name of table without the v_ prefix.
    
    * How to create the primary key name
    * If the table name is v_users take remove the 'v_', make it non-plural and add '_uuid' to the end of the field name. In this example the primary key would be user_uuid

Code Documentation

http://www.phpdoc.org/
