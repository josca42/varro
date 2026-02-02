# Popover (Dropdown) Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-popover>
    <button x-popover:button>Company</button>

    <ul x-popover:panel>
        <a href="#about">About Us</a>
        <a href="#team">Team</a>
    </ul>
</div>
```

## Adding an overlay

Sometimes, you may want to de-emphasize the webpage behind a dropdown when it is open. In these cases, you can use the optional x-popover:overlay on an element to toggle the overlay along with the Popover.

Because these directives are headless, it is still up to you to style the overlay as you wish (usually a semi-transparent darker background color).

```html
<div x-popover>
    <button x-popover:button>...</button>

    <div x-popover:overlay></div>

    <ul x-popover:panel>
        ...
    </ul>
</div>
```

## Grouping Popovers

If you were building something like a navbar with multiple dropdowns inside it, you may want them to behave differently. For example, if you tab through one menu onto another you may want the previous menu to remain open until you open an entirely different menu.

This functionality is provided with the x-popover:group directive. By adding this to the an element wrapping the x-popover elements, you are making them aware of each other and the functionality will reflect that.

```html
<div x-popover:group x-data>
    <div x-popover>
        ...
    </div>

    <div x-popover>
        ...
    </div>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| [Enter or Space] | Toggles the Popover panel when the x-popover:button is in focus |
| [Escape] | Closes the Popover |
| [Tab] | Cycles through the tabbable elements inside the Popover (when it is open) |
| [Shift] + [Tab] | Cycles backwards through the tabbable elements inside the Popover (when it is open) |

## API Reference

### x-popover

The main directive for the Popover component.

| Attribute | Description |
|-----------|-------------|
| x-model | Used to control whether the popover is open using outside data |

### $popover

The magic property for manually controlling the state of the Popover component. You can access this property anywhere within the Popover.

| Properties | Description |
|------------|-------------|
| isOpen | A property that returns a boolean value whether the popover is open or not |
| open() | A method to open the popover |
| close() | A method to close the popover |

### x-popover:button

Used to toggle the Popover open/closed state.

### x-popover:overlay

Used to specify which element should be used as the Popover overlay.

### x-popover:panel

Used to specify which element should be used as the Popover visible panel.

| Attributes | Description |
|------------|-------------|
| focus | If this attribute is added, the panel first element will receive focus when it is opened. Also, when inside a x-popover:group, this panel will close when tabbed away instead of staying open when focusing other Popovers inside the group. |
| static | If this attribute is added, the component will render statically (in a permanent open state) and will allow you to control its visibility externally however you wish. |

### x-popover:group

Used to specify a group of Popovers.