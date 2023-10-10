# Using Cylc with `rnr-refresh`

## Major Differences Between Cylc 7 and 8
If you were using UFS-RNR, then you are likely accustomed to cylc 7.9.3, but
we have updated to cylc 8.2.1 (as of this writing) and will keep up with newer
versions of Cylc going forward.  So, here's some major changes that may affect
how you use this software.  

### Documentation Links
* [Cylc 8 Migration Guide](https://cylc.github.io/cylc-doc/latest/html/7-to-8/index.html)
    * [Summary of Major Changes](https://cylc.github.io/cylc-doc/latest/html/7-to-8/summary.html)
    * [Cheat Sheet](https://cylc.github.io/cylc-doc/latest/html/7-to-8/cheat-sheet.html)
    * [Full List of Command Changes](https://cylc.github.io/cylc-doc/latest/html/7-to-8/major-changes/cli.html#full-list-of-command-changes)
    * [Detailed Description of Major Changes](https://cylc.github.io/cylc-doc/latest/html/7-to-8/major-changes/index.html)
    * [Cylc 8.2 Caveats](https://cylc.github.io/cylc-doc/latest/html/7-to-8/caveats.html)
* You can also practice the full [Tutorial](https://cylc.github.io/cylc-doc/latest/html/tutorial/index.html).

### Shortlist of Major Changes Affecting Us
The following list is not intended to replace any Cylc 8 documentation, and is certainly not comprehensive.
Instead, it is intended as a starting point for navigating switching to Cylc 8 commands in `rnr-refresh` if you were accustomed to Cylc 7 commands in `UFS-RNR`.

* **Workflows** are now the focus.  From the Cylc 8 Glossary entry for [cylc workflow](https://cylc.github.io/cylc-doc/latest/html/glossary.html#term-cylc-workflow),
"suites" are now called “workflows”.
   * The `suite.rc` file is now replaced by the [`flow.cylc` file](https://cylc.github.io/cylc-doc/latest/html/tutorial/scheduling/graphing.html)
   * Typical command flow is different for workflows:
      * First, validate a workflow with `cylc validate` to check the `flow.cylc` file (this is also done automatically during `cylc play`) conforms to legal definitions for Cylc 8.  This will output which version of Cylc it is valid for.  Also check out `cylc lint` in [the docs](https://cylc.github.io/cylc-doc/latest/html/user-guide/writing-workflows/configuration.html#module-cylc.flow.scripts.lint) for more detailed output on errors.
      * Second, install (replaced `cylc register`) the workflow with `cylc install`.  Workflows are installed  to the default cylc location in `~/cylc-run/<workflow_name>`.
      * Third (and finally), run the workflow with `cylc play`.  This is also the command for restarting.
   * Optionally, check out [Compound Commands](https://cylc.github.io/cylc-doc/latest/html/user-guide/compound-commands.html#compoundcommands) for a shortcut `cylc vip`.
   * Also check out the [Workflow Configuration](https://cylc.github.io/cylc-doc/latest/html/user-guide/writing-workflows/configuration.html) doc to understand how to write a 
* **Monitoring** has changed entirely (i.e. there is no `cylc monitor` command) and has new [Cylc UIs](https://cylc.github.io/cylc-doc/8.0.0/html/7-to-8/major-changes/ui.html).
     There is now a terminal user interface (`cylc tui <workflow_name>`) and a GUI.
* **Platforms** are a new feature which replace the task job and remote configuration sections
   * Platforms now have their own configuration files
   * ...
* **Tasks** have also been overhauled:
   * ...


## How `rnr-refresh` Is Configured With Cylc 8

### Global Configuration
[Global Configuration](https://cylc.github.io/cylc-doc/latest/html/reference/config/global.html#global-configuration)

### Platform Configurations
[Platforms](https://cylc.github.io/cylc-doc/latest/html/7-to-8/major-changes/platforms.html)
[Platform Configuration](https://cylc.github.io/cylc-doc/latest/html/reference/config/writing-platform-configs.html)

### Scheduler Configuration
[Scheduler Configuration](https://cylc.github.io/cylc-doc/latest/html/user-guide/writing-workflows/scheduler.html)

### Workflow Configurations
[Workflow Configuration](https://cylc.github.io/cylc-doc/latest/html/reference/config/workflow.html#workflow-configuration)


### Task Configurations
[Task Configuration](https://cylc.github.io/cylc-doc/latest/html/user-guide/writing-workflows/runtime.html)
