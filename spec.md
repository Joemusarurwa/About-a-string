# Specification

A compliant README must satisfy all the requirements listed below.

**Requirements:**

- Be called README.md (with capitalization).
- Be a valid Markdown file.
- Sections must appear in order given below. Optional sections may be omitted.
- Sections must have the titles listed below, unless otherwise specified. If the README is in another language, the titles must be translated into that language.
- Must not contain broken links.
- If there are code examples, they should be linted in the same way as the code is linted in the rest of the project.

## Table of Contents

_Note: Not all of these sections are mandatory. The status for each section is given below._

- [Sections](#sections)
  - [Title](#title)
  - [Banner](#banner)
  - [Badges](#badges)
  - [Short Description](#short-description)
  - [Long Description](#long-description)
  - [Table of Contents](#table-of-contents-1)
  - [Install](#install)
  - [Usage](#usage)
  - [API](#api)
  - [Maintainers](#maintainers)
  - [License](#license)

## Sections

### Title
**Status:** Required.

**Requirements:**
- Title must match the repository, folder and package manager names - or it may have another, relevant title with the repository, folder, and package manager title next to it in italics and in parentheses. For instance:

  ```markdown
  # Standard Readme Style _(standard-readme)_
  ```

**Suggestions:**
- Financial Times ES README Template Public
- EC2 Powercycle
- Enterprise Services

### Banner
**Status:** Optional.

**Requirements:**
- Must not have its own title.
- Must link to local file/image in current repository.
- Must appear directly after the title.

### Badges
**Status:** Optional.

**Requirements:**
- Must not have its own title.
- Must be newline delimited.

**Suggestions:**
- Use http://shields.io or a similar service to create and host the images.
- Add the [Standard Readme badge](https://github.com/RichardLitt/standard-readme#badge) if your README follows these guidelines.

### Table of Contents
**Status:** Required; optional for READMEs shorter than 100 lines.

**Requirements:**
- Must link to all Markdown sections in the file.
- Must start with the next section; do not include the title or Table of Contents headings.
- Must be at least one-depth: must capture all `##` headings.

**Suggestions:**
- May capture third and fourth depth headings. If it is a long ToC, these are optional.

### Short Description
**Status:** Required.

**Requirements:**
- Must not have its own title.
- Must be less than 120 characters.
- Must be on its own line.
- Must match GitHub's description (if on GitHub).

**Suggestions:**
- This will be specific to the repository so no suggestion given.

### Long Description
**Status:** Optional.

**Requirements:**
- Must not have its own title.
- If any of the folder, repository, or package manager names do not match, there must be a note here as to why.

**Suggestions:**
- If too long, consider moving less important information to a [Background](#background) section.
- Cover the main reasons for building the repository.
- "This should describe your module in broad terms,
generally in just a few paragraphs; more detail of the module's
routines or methods, lengthy code examples, or other in-depth
material should be given in subsequent sections.

### Install
**Status:** Required by default, optional for [documentation repositories](#definitions).

**Requirements:**
- Code block illustrating how to install.

**Subsections:**
- `Dependencies`. Required if there are unusual dependencies or dependencies that must be manually installed.

**Suggestions:**
- Link to prerequisite sites for programming language: [npmjs](https://npmjs.com), [godocs](https://godoc.org), etc.
- Include any system-specific information needed for installation.
- An `Updating` section would be useful for most packages, if there are multiple versions which the user may interface with.

### Usage
**Status:** Required by default, optional for documentation repositories.

**Requirements:**
- Code block illustrating common usage.
- If CLI compatible, code block indicating common usage.
- If importable, code block indicating both import functionality and usage.

**Subsections:**
- `CLI`. Required if CLI functionality exists.

**Suggestions:**
- Cover basic choices that may affect usage: for instance, if JavaScript, cover promises/callbacks, ES6 here.
- If relevant, point to a runnable file for the usage code.

### API
**Status:** Optional.

**Requirements:**
- Describe exported functions and objects.

**Suggestions:**
- Describe signatures, return types, callbacks, and events.
- Cover types covered where not obvious.
- Describe caveats.

### Monitoring
**Status:** Optional.

**Requirements:**
- Provide links to necessary monitoring for the module.

**Suggestions:**
- Grafana Dashboards
- Heimdall Checks
- Any other necessary monitoring.

### Maintainer(s)
**Status**: Optional.

**Requirements:**
- List maintainer(s) for a repository, along with one way of contacting them (e.g. GitHub link or email).

**Suggestions:**
- This should be a small list of people in charge of the repo. This should not be everyone with access rights, such as an entire organization, but the people who should be pinged and who are in charge of the direction and maintenance of the repository.
- You may continue listing past maintainers for the repo, but make a note of this next to their name.

### License
**Status:** Required.

**Requirements:**
- State license full name or identifier, as listed on the  [SPDX](https://spdx.org/licenses/) license list. For unlicensed repositories, add `UNLICENSED`. For more details, add `SEE LICENSE IN <filename>` and link to the license file. (These requirements were adapted from [npm](https://docs.npmjs.com/files/package.json#license)).
- State license owner.
- Must be last section.
