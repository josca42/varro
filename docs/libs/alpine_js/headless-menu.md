# Menu (Dropdown) Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data>
    <div x-menu>
        <button x-menu:button>
            Options
        </button>

        <div x-menu:items>
            <a x-menu:item href="#edit">
                Edit
            </a>
            <a x-menu:item href="#copy">
                Copy
            </a>
            <a x-menu:item disabled href="#delete">
                Delete
            </a>
        </div>
    </div>
</div>
```

## Styling the active item

You can apply custom styling to the active item by using the $menuItem.isActive boolean and setting any classes you need.

```html
<a x-menu:item href="#edit"
   :class="$menuItem.isActive && 'bg-cyan-500/10 text-gray-900'"
>
    Edit
</a>
```

## Disabling an item

You can disable an item by adding the disabled attribute to a x-menu:item element. This will make this item un-selectable and will be skipped when navigating through items using the arrow-keys.

```html
<a x-menu:item href="#edit" disabled>
    Edit
</a>
```

You can also access the disabled state of an item anywhere inside that item using $menuItem.isDisabled like so:

```html
<a x-menu:item href="#edit" disabled
   :class="$menu.isDisabled && 'disabled'"
>
    Edit
</a>
```

## Controlling the open state manually

By default, the Menu component controls its open state internally. If you would rather control the open state externally, you may use x-model on the x-menu element.

```html
<div x-data="{ open: false }">
    <div x-menu x-model="open">
        ...
    </div>
</div>
```

## Transitions

The Menu component works well with Alpine transitions feature. Just add x-transition to the x-menu:items element with the appropriate origin modifier based on your styling to apply smooth open/close transitions.

```html
<div x-data>
    <div x-menu>
        ...
        <div x-menu:items
             x-transition.origin.top.right
             class="absolute right-0 ..."
        >
            ...
        </div>
    </div>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| Enter/Space | Open the menu when closed or select the focused item when the menu is open |
| Escape | Close the menu |
| Arrow Keys | Focuses the next/previous non-disabled item |
| Home/PageUp | Focuses the first non-disabled item |
| End/PageDown | Focuses the last non-disabled item |
| A-z | Focuses the first item matching the keyboard input |

## API Reference

### x-menu

The main directive for the Menu component, used to contain the behavior for the menu, its button, and items.

| Attributes | Description |
|------------|-------------|
| x-model | Used to control whether the menu is open using outside data |

### x-menu:button

Used to specify the button that toggles the menu.

### x-menu:items

Used to specify the menu contents. This is the element that will be toggled open and closed.

### x-menu:item

Used to specify a specific menu item.

### $menuItem

A magic variable that exposes information about the current state of the closest menu item (element containing x-menu:item).

| Properties | Description |
|------------|-------------|
| isActive | A boolean used to determine whether or not an item is currently active |
| isDisabled | A boolean used to determine whether or not an item is currently disabled |