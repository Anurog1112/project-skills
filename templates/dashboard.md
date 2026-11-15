# Selected layout — Dashboard

Use when the user needs to inspect, compare, filter, or act on data. This is a screen blueprint to adapt to existing data and the requested decision.

## Structure

- Title and current scope, such as date range, team, project, or status.
- Only the summary metrics needed for the user's decision, with meaningful names and units.
- Filters and search near the content they affect. Show the active filters and a clear reset when useful.
- A chart when it makes a comparison or trend easier to understand. Keep labels and units readable and offer relevant exact values.
- A record table or list with the necessary columns, status, and row actions.
- Loading, empty, no-matching-results, and error states appropriate to the data flow.

## Design and behavior

Use existing project records or a confirmed data source. Derive summaries and charts from the same filtered dataset so totals remain consistent. Label requested sample data as a demonstration. Distinguish a missing value from zero.

Use alignment, restrained emphasis, readable numeric formats, and consistent status labels. On narrow screens, adapt filters and record presentation, or provide a clearly scoped table scroll area while the rest of the page fits.

## User checks

- Filters update the intended metrics, chart, and records consistently.
- Totals can be checked against the visible source records.
- Empty results have a useful next action, and existing record actions still work.
