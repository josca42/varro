I am re-creating an analytics environment for statistics about Denmark. I'm starting out by copying tables from Denmark Statistics. The structure of these tables is that there are fact tables and there are dimension tables. You can interact with the fact and dimension tables through the tables skill.

The tables have also been structured into a subject hierarchy. You can access this using the subjects skill. Through this skill you can also access metadata about the different tables such as the unique values of the different columns. If you want to see all unique values of dimension columns you can use table-info in the subject skill.

Put scripts you make in agents/scripts and markdown files in agents/markdown