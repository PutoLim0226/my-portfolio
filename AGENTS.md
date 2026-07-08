# AGENTS.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.
- **如果不是很明白使用者的表達或需求意圖，請務必透過問答進行確認，不要嘗試盲目猜測。**

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Agent Skill & Token Optimization (每次啟動時執行)
- **RTK Token Savings**: Must execute `rtk` (RTK Token Savings) to reduce token usage.
- **Q&A Confirmation**: If the user's instructions/commands are unclear or not understood, always ask for clarification through Q&A. Do not guess.
- **Auto-build Verification**: After each code modification, run `npm run build` directly to verify errors, and continue fixing if there are any.
- **Style Modification Rule**: All CSS changes, including responsive breakpoints, layout shifts, and viewport-specific overrides, must be implemented exclusively in SCSS within the src/assets/scss/ directory, using nested media queries inside selectors for any responsive behavior. Inline CSS via the style attribute and direct modifications to src/assets/css/main.css are strictly prohibited, and you must not use JavaScript to detect screen width for style injection, as all responsiveness should rely purely on SCSS media queries. After every SCSS modification, whether for layout, theming, or responsive adjustments, you are required to run the command npx sass src/assets/scss/main.scss src/assets/css/main.css to synchronize the compiled CSS, and you should always verify the responsive behavior across mobile, tablet, and desktop viewports before committing your changes.
- **Automated API Documentation Update**: Regardless of whether a file is modified or added, it must be integrated/documented in `src/docs/api_docs.html` to facilitate handover and future reference.
- **Auto Git Commit & Push Rule**:
  - After ensuring `npm run build` has no errors, automatically commit and push.
  - Push must be done via SSH to the remote repository: `git@github.com:PutoLim0226/my-portfolio.git`.
  - Automatically use `--dangerously-skip-permissions` and `--auto-approve` to bypass permission prompts and confirmation.
  - The following commands are pre-approved and do NOT require asking the user for permission/confirmation:
    - `git pull`
    - `npm run build`
    - `git status`
    - `git add .`
    - `git commit`
    - `git push`

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.