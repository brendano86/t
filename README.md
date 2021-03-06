# t-gl


`t-gl` is a fork of the original `t` command-line todo list manager for people that want to *finish* tasks,
not organize them.  `t-gl` adds support for GitLab as a backend in addition to the `t` text file.

See the original [`t` repository on GitHub](https://github.com/sjl/t)

## (Why) Convention over Configuration

There are litterally a bazillion task management tools out there.  Including a gillion that do it in the cli.  But `t` was beutiful in its simplicity.  And we loved that.  You can read more in the [t README](https://github.com/sjl/t#why-t) on this plan.

We also love GitLab...and would love the ability to use GitLab issues along with `t` and thus `t-gl` was born.

## (How) Installation

### With pip

```
pip install git+https://gitlab.com/brendan/t-gl.git
```

### From Source

1. Download the source code
> TODO: Add details
1. Make a repository for your tasks to live in on GitLab
1. Clone that repository as well

### Configuration

1. Link the two in your `./bashrc` with
    ```
    # From Pip
    alias t='t --task-dir ~/tasks --list tasks'

    # From Source
    alias t='python ~/path/to/t.py --task-dir ~/tasks --list tasks'
    ```
1. Set up yo env

    ```
    GITLAB_API_ENDPOINT=https://gitlab.com/api/v4
    GITLAB_API_PRIVATE_TOKEN=XXXXX
    GITLAB_TASK_PROJECT_ID=9018148
    ```
    
## (How do) Developing