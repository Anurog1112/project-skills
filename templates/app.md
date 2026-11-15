# Selected layout — Web App

Use for completing a task, such as a booking form, tracker, calculator, task list, or simple record editor. This is a workflow blueprint to adapt to the current MVP.

## Structure

- Screen title that explains the current task and any important context.
- Task area with labelled inputs, clear grouping, defaults based on existing requirements, and a visible primary action.
- Validation close to the affected field with guidance the user can act on.
- Result or record area showing the outcome of the user's action and the next useful step.
- Relevant edit, delete, cancel, reset, or back actions with consistent labels and feedback.
- Empty, success, and error states for the actual user flow.

## Design and behavior

Follow the complete flow from input to result. Validate the requested data before adding it, prevent unintended duplicate actions, and keep visible records and counts consistent. Preserve the current storage behavior unless changing persistence is part of the request.

Use clear labels, a readable form width, consistent field spacing, and touch-friendly controls. Preserve entered data when validation fails. Keep keyboard use and focus after actions sensible.

## Example adaptation

For an existing reservation MVP, connect the booking form, validation, reservation list, totals, and existing cancellation flow. Improve the requested Wish within that flow. Describe a frontend demonstration according to what it actually saves and validates.

## User checks

- Valid input completes the task and produces the expected visible result.
- Invalid input produces useful guidance while preserving the user's work.
- Existing edit/delete/reset actions and phone/desktop layouts remain usable.
