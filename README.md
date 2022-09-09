# gh-csaudit

GitHub Code Scanning Audit CLI Tool

## Usage

```bash
gh extension install GeekMasher/gh-csaudit
gh csaudit --help

# Install deps
pip3 install requests tabulate
```

#### Run on a single repository

```bash
gh csaudit -r GeekMasher/Pixi
```

<details>
<summary>Example Output</summary>
<p> 

<pre>

 _____  _____  ___            _ _ _
/  __ \/  ___|/ _ \          | (_) |
| /  \/\ `--./ /_\ \_   _  __| |_| |_
| |     `--. \  _  | | | |/ _` | | __|
| \__/\/\__/ / | | | |_| | (_| | | |_
 \____/\____/\_| |_/\__,_|\__,_|_|\__|   v0.1.0

        Build by GitHub Field Security Specialist Team

================================================================

Tool                       Version                                         Datetime
-------------------------  ----------------------------------------------  --------------------
CodeQL                     2.7.3                                           2022-01-23T06:08:36Z
codeql/javascript-queries  0.0.5+ddd4ccbb4b39adf3c2427088f4876432202c4eaa

Rule Name / ID                                     Rule Description                                                            Rule Priority
-------------------------------------------------  --------------------------------------------------------------------------  ---------------
js/angular/disabling-sce                           Disabling SCE                                                               warning
js/angular/double-compilation                      Double compilation                                                          warning
js/angular/insecure-url-whitelist                  Insecure URL whitelist                                                      warning
js/bad-code-sanitization                           Improper code sanitization                                                  error
js/bad-tag-filter                                  Bad HTML filtering regexp                                                   warning
js/biased-cryptographic-random                     Creating biased random numbers from a cryptographically secure source.      warning
js/build-artifact-leak                             Storage of sensitive information in build artifact                          error
js/clear-text-cookie                               Clear text transmission of sensitive cookie                                 warning
js/clear-text-logging                              Clear-text logging of sensitive information                                 error
js/clear-text-storage-of-sensitive-data            Clear text storage of sensitive information                                 error
js/client-exposed-cookie                           Sensitive server cookie exposed to the client                               warning
js/client-side-unvalidated-url-redirection         Client-side URL redirect                                                    error
js/code-injection                                  Code injection                                                              error
js/command-line-injection                          Uncontrolled command line                                                   error
js/cors-misconfiguration-for-credentials           CORS misconfiguration for credentials transfer                              error
js/cross-window-information-leak                   Cross-window communication with unrestricted target origin                  error
js/disabling-certificate-validation                Disabling certificate validation                                            error
js/disabling-electron-websecurity                  Disabling Electron webSecurity                                              error
js/double-escaping                                 Double escaping or unescaping                                               warning
js/enabling-electron-insecure-content              Enabling Electron allowRunningInsecureContent                               error
js/exposure-of-private-files                       Exposure of private files                                                   warning
js/file-access-to-http                             File data in outbound network request                                       warning
js/hardcoded-credentials                           Hard-coded credentials                                                      warning
js/hardcoded-data-interpreted-as-code              Hard-coded data interpreted as code                                         error
js/host-header-forgery-in-email-generation         Host header poisoning in email generation                                   error
js/html-constructed-from-input                     Unsafe HTML constructed from library input                                  error
js/http-to-file-access                             Network data written to file                                                warning
js/identity-replacement                            Replacement of a substring with itself                                      warning
js/incomplete-hostname-regexp                      Incomplete regular expression for hostnames                                 warning
js/incomplete-html-attribute-sanitization          Incomplete HTML attribute sanitization                                      warning
js/incomplete-multi-character-sanitization         Incomplete multi-character sanitization                                     warning
js/incomplete-sanitization                         Incomplete string escaping or encoding                                      warning
js/incomplete-url-scheme-check                     Incomplete URL scheme check                                                 warning
js/incomplete-url-substring-sanitization           Incomplete URL substring sanitization                                       warning
js/incorrect-suffix-check                          Incorrect suffix check                                                      error
js/indirect-command-line-injection                 Indirect uncontrolled command line                                          warning
js/insecure-download                               Download of sensitive file through insecure connection                      error
js/insecure-randomness                             Insecure randomness                                                         warning
js/insufficient-key-size                           Use of a weak cryptographic key                                             warning
js/insufficient-password-hash                      Use of password hash with insufficient computational effort                 warning
js/log-injection                                   Log injection                                                               error
js/loop-bound-injection                            Loop bound injection                                                        warning
js/missing-rate-limiting                           Missing rate limiting                                                       error
js/missing-token-validation                        Missing CSRF middleware                                                     error
js/password-in-configuration-file                  Password in configuration file                                              warning
js/path-injection                                  Uncontrolled data used in path expression                                   error
js/polynomial-redos                                Polynomial regular expression used on uncontrolled data                     warning
js/prototype-polluting-assignment                  Prototype-polluting assignment                                              warning
js/prototype-pollution                             Prototype-polluting merge call                                              error
js/prototype-pollution-utility                     Prototype-polluting function                                                warning
js/redos                                           Inefficient regular expression                                              error
js/reflected-xss                                   Reflected cross-site scripting                                              error
js/regex-injection                                 Regular expression injection                                                error
js/regex/missing-regexp-anchor                     Missing regular expression anchor                                           warning
js/remote-property-injection                       Remote property injection                                                   warning
js/request-forgery                                 Uncontrolled data used in network request                                   error
js/resource-exhaustion-from-deep-object-traversal  Resources exhaustion from deep object traversal                             warning
js/sensitive-get-query                             Sensitive data read from GET request                                        warning
js/server-crash                                    Server crash                                                                warning
js/server-side-unvalidated-url-redirection         Server-side URL redirect                                                    warning
js/session-fixation                                Failure to abandon session                                                  warning
js/shell-command-constructed-from-input            Unsafe shell command constructed from library input                         error
js/shell-command-injection-from-environment        Shell command built from environment values                                 warning
js/sql-injection                                   Database query built from user-controlled sources                           error
js/stack-trace-exposure                            Information exposure through a stack trace                                  warning
js/stored-xss                                      Stored cross-site scripting                                                 error
js/summary/lines-of-code                           Total lines of JavaScript and TypeScript code in the database               warning
js/summary/lines-of-user-code                      Total lines of user written JavaScript and TypeScript code in the database  warning
js/tainted-format-string                           Use of externally-controlled format string                                  warning
js/template-object-injection                       Template Object Injection                                                   error
js/type-confusion-through-parameter-tampering      Type confusion through parameter tampering                                  error
js/unnecessary-use-of-cat                          Unnecessary use of `cat` process                                            error
js/unsafe-deserialization                          Deserialization of user-controlled data                                     warning
js/unsafe-dynamic-method-access                    Unsafe dynamic method access                                                error
js/unsafe-external-link                            Potentially unsafe external link                                            warning
js/unsafe-html-expansion                           Unsafe expansion of self-closing HTML tag                                   warning
js/unsafe-jquery-plugin                            Unsafe jQuery plugin                                                        warning
js/unvalidated-dynamic-method-call                 Unvalidated dynamic method call                                             warning
js/useless-regexp-character-escape                 Useless regular-expression character escape                                 error
js/user-controlled-bypass                          User-controlled bypass of security check                                    error
js/weak-cryptographic-algorithm                    Use of a broken or weak cryptographic algorithm                             warning
js/xml-bomb                                        XML internal entity expansion                                               warning
js/xpath-injection                                 XPath injection                                                             error
js/xss                                             Client-side cross-site scripting                                            error
js/xss-through-dom                                 DOM text reinterpreted as HTML                                              warning
js/xss-through-exception                           Exception text reinterpreted as HTML                                        warning
js/xxe                                             XML external entity expansion                                               error
js/zipslip                                         Arbitrary file write during zip extraction ("Zip Slip")                     error

================================================================

Completed
</pre>

</p>
</details>
