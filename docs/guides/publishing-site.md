# Publishing the documentation website

[← Documentation home](../README.md) · [← GitHub repository](https://github.com/lilouwen/homelab)

## What is prepared

The repository contains a MkDocs Material site with a searchable service catalog, Mermaid diagrams, copyable command snippets, a dark/light theme and technical pages linked from the original Markdown documentation.

**The site is not automatically live merely because this configuration exists.** GitHub Pages must be enabled in the repository settings first.

## Activate GitHub Pages

1. Open the repository **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions**.
3. Open the repository **Actions** tab, then select **Documentation website**.
4. Choose **Run workflow** on the `main` branch.
5. Verify the build and deployment jobs succeeded before sharing the site address.

The intended project-site URL is `https://lilouwen.github.io/homelab/`, but it should not be presented as active until GitHub confirms a successful deployment.

## Editing the site

Update a relevant Markdown file in `docs/`; the site generator automatically includes it on the next build. Use `mkdocs.yml` to change the menu order.

### Optional local preview

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

Open the local preview address printed by the command. For a production build, use:

```bash
mkdocs build --clean --site-dir site
```

## Deployment safeguards

- The build runs for ordinary pushes and pull requests; deployment only runs when explicitly requested with **Run workflow** on `main`.
- The publishing job requests GitHub Pages permissions; normal documentation checks remain read-only.
- No VPN keys, server access, databases or personal files are needed for publication.
- Only sanitized documentation content should be committed to the public repository.
- Broken local Markdown navigation is also checked by the separate `Documentation quality` workflow.

[← Documentation home](../README.md)
