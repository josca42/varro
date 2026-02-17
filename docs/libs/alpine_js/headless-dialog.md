# Dialog (Modal) Component - Alpine.js

Building a modal with Alpine might appear as simple as putting x-show on an element styled as a modal. Unfortunately, much more goes into building a robust, accessible modal. The following functionality is considered essential:

- Ability to close the modal on escape
- Close when you click outside the modal onto the background overlay
- Trap focus within the modal to prevent focusing the page behind it
- Disable scrolling the background when modal is active
- Proper accessibility HTML attributes such as role="dialog"

For these cases, the x-dialog family of directives exists.

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data="{ open: false }">
    <button x-on:click="open = true" class="...">Open Modal</button>

    <div x-dialog x-model="open" class="...">
        <div x-dialog:overlay class="..."></div>

        <div x-dialog:panel class="...">
            <h2 x-dialog:title class="...">Some modal</h2>

            <button x-on:click="$dialog.close()" class="...">Close</button>
        </div>
    </div>
</div>
```

## Adding an overlay

Often, you want to distinguish a modal from the page behind it. In these cases, you can use the optional x-dialog:overlay on an element to give it extra behavior such as closing the modal when it is clicked.

Because these directives are headless, it is still up to you to style the overlay as you wish (usually a semi-transparent darker background color).

```html
<div x-dialog>
    <div x-dialog:overlay></div>

    <div x-dialog:panel>
        ...
    </div>
</div>
```

## Adding a title and description

Modals often have titles and description text that would be helpful for a screenreader. To properly tell screenreaders and other assistive technologies about these titles and descriptions, you can use either or both of the x-dialog:title and x-dialog:description directives.

```html
<div x-dialog>
    <h2 x-dialog:title>...</h2>
    <p x-dialog:description>...</p>
</div>
```

## Specifying initial focus

By default, the dialog will focus the first focusable element when the dialog is shown. If you wish to customize which element is focused, you can do so using the :initial-focus property:

```html
<div x-dialog :initial-focus="$refs.button">
    ...
    <button type="button" x-ref="button">Submit</button>
</div>
```

## Static rendering

If you wish to opt-out of the Dialog component internal open/closed state and simply render the dialog statically on the page, you can use the static attribute:

```html
<div x-data="{ open: false }">
    <button @click="open = true">Open</button>

    <template x-if="open">
        <div x-dialog static>
            ...
        </div>
    </template>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| [Escape] | Closes the dialog |
| [Tab] | Cycles through the tabbable elements inside the dialog (when it is open) |
| [Shift] + [Tab] | Cycles backwards through the tabbable elements inside the dialog (when it is open) |

## API Reference

### x-dialog

The main directive for the Dialog component.

| Attribute | Description |
|-----------|-------------|
| x-model | Used to control the state of the Dialog component. It is two-way bound, so its value is controlled from both inside the component and outside |
| static | If this attribute is added, the component will render statically and will not be toggled on and off using the Dialog component internal state |

### $dialog

The magic property for manually controlling the state of the Dialog component. You can access this property anywhere within the dialog.

| Properties | Description |
|------------|-------------|
| isOpen | A property that returns a boolean value whether the dialog is open or not |
| close() | A method to close the dialog |

### x-dialog:overlay

Used to specify which element should be used as the dialog overlay.

### x-dialog:panel

Used to specify which element should be used as the dialog visible panel. This exists to distinguish the panel element from a sibling overlay element. By adding this to an element, it will automatically close the dialog when the user clicks anywhere outside it, whether or not you are using a background overlay.

### x-dialog:title

Used to distinguish the dialog title.

### x-dialog:description

Used to distinguish the dialog description.