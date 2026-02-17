# Listbox (Select) Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data="{ value: null }">
    <div x-listbox x-model="value">
        <button x-listbox:button>
            Select Framework
        </button>

        <ul x-listbox:options>
            <li x-listbox:option value="laravel">
                Laravel
            </li>
            <li x-listbox:option value="rails">
                Ruby on Rails
            </li>
            <li x-listbox:option value="phoenix" disabled>
                Phoenix
            </li>
        </ul>
    </div>

    Selected: <span x-text="value"></span>
</div>
```

## Styling the selected, active, and disabled items

You can apply custom styling to the selected, active, and disabled items by using the $listboxOption.isSelected, $listboxOption.isActive, and $listboxOption.isDisabled booleans respectively and setting any classes you need.

```html
<li x-listbox:option
    :class="{
        'bg-cyan-500/10': $listboxOption.isActive,
        'opacity-50 cursor-not-allowed': $listboxOption.isDisabled,
    }"
    ...>
    <span>Laravel</span>
    <span x-show="$listboxOption.isSelected">&check;</span>
</li>
```

## Disabling an option

You can disable an option by adding the disabled attribute to a x-listbox:option element. This will make this option un-selectable and will be skipped when navigating through options using the arrow-keys.

```html
<li x-listbox:option disabled>
    <span>Laravel</span>
</li>
```

## Manually showing/hiding the listbox

The Listbox component manages its open state internally and automatically shows/hides the options based on that state.

If you would prefer to keep the x-listbox:options element open permanently, you may add the static attribute on the x-listbox:options element.

You can also access the internally managed open state using $listbox.isOpen.

```html
<div x-data="{ value: null }">
    <div x-listbox x-model="value">
        <button x-listbox:button>...</button>

        <div x-show="$listbox.isOpen">
            <ul x-listbox:options static>
                ...
            </ul>
        </div>
    </div>
</div>
```

## Transitions

The Listbox component works well with Alpine transitions feature. Just add x-transition to the x-listbox:options element with the appropriate origin modifier based on your styling to apply smooth open/close transitions.

```html
<div x-data="{ value: null }">
    <div x-listbox x-model="value">
        <button x-listbox:button>...</button>

        <ul x-listbox:options x-transition.origin.top.right>
            ...
        </ul>
    </div>
</div>
```

## Selecting multiple values

By default, the Listbox component only allows a single option to be selected at a time. If you would like the user to be able to select multiple options, pass a multiple prop to the x-listbox element.

```html
<div x-data="{ value: [] }">
    <div x-listbox x-model="value" multiple>
        ...
    </div>
</div>
```

When selecting an option while multiple is enabled, the option value will be added to an array and the x-listbox:options will remain open until the esc key is pressed or the user clicks outside the Listbox.

## Binding objects as values

Traditional HTML form inputs do not support using objects as values, but the x-listbox component does.

In order for the component to work correctly, ensure that you always use the same instance of the value objects, otherwise the component may not test equality correctly.

To make it easier to work with different instances of the same object, you can use the by prop to compare the objects by a particular property instead of comparing objects by their identity:

```html
<div x-listbox x-model="framework" by="id">
    ...
</div>
```

## Using as an HTML form input

If you are using the component inside an HTML form, you may pass a name prop to the x-listbox element and Alpine will create a hidden input that is kept in sync with the value of the Listbox.

```html
<div x-data="{ value: null }">
    <div x-listbox name="framework" x-model="value">
        ...
    </div>
</div>
```

## Using as an uncontrolled component

If no x-model is bound to the x-listbox element, the component will manage its own state automatically. In this case, you may set a default-value attribute on the x-listbox element to specify which option should be checked when the page is initially loaded.

```html
<div x-data>
    <div x-listbox default-value="laravel">
        ...
    </div>
</div>
```

## Adding a custom label

Headless Alpine will use the x-listbox:button contents as the default label. If you would like more control over the label, you may add x-listbox:label to an element to use it as the label for the Listbox.

```html
<div x-data="{ value: 'laravel' }">
    <div x-listbox x-model="value">
        <span x-listbox:label>Backend framework</span>

        <ul x-listbox:options>
            ...
        </ul>
    </div>
</div>
```

## Displaying the component horizontally

By default, the Listbox assumes you are displaying the options vertically, so it enables navigation via the up and down arrow keys. If you have styled your options to be displayed horizontally, pass a horizontal prop to the x-listbox element, and the Listbox will enable navigation via the left and right arrow keys instead.

```html
<div x-data="{ value: null }">
    <div x-listbox x-model="value" horizontal>
        ...
    </div>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| Enter/Space | Open the Listbox when closed or select the focused option when the Listbox is open |
| Escape | Close the Listbox |
| Arrow Keys | Focuses the next/previous non-disabled item |
| Home/PageUp | Focuses the first non-disabled item |
| End/PageDown | Focuses the last non-disabled item |
| A-z | Focuses the first option matching the keyboard input |

## API Reference

### x-listbox

The main directive for the Listbox component, used to contain the behavior for the Listbox, its button, label, and options.

| Attributes | Description |
|------------|-------------|
| x-model | Used to control which option is currently selected using outside data |
| name | Used to create a hidden input with the passed name that can be used for traditional HTML form submissions |
| disabled | Used to disable the entire component and prevent opening the options panel and selecting items |
| default-value | A mixed value used to set the default selected option |
| multiple | A boolean used to allow users to select multiple options |
| horizontal | A boolean used to indicate that the options will be displayed horizontally and enable navigation via the left and right arrow keys |
| by | A string key or function used to set the key or comparison function the Listbox uses to compare options for the active/selected states |

### $listbox

A magic variable that exposes information about the current state of the Listbox (element containing x-listbox).

| Properties | Description |
|------------|-------------|
| value | The currently selected value |
| isOpen | A boolean used to determine whether or not the options panel is open |
| isDisabled | A boolean used to determine whether or not the entire component is disabled |

### x-listbox:button

Used to specify the button that will open/close the x-listbox:options panel.

### x-listbox:options

Used to specify the panel that contains the options. This is the element that will be opened and closed when the x-listbox:button is clicked.

| Attributes | Description |
|------------|-------------|
| static | A boolean used to disable the internal open/closed state so you can manually show or hide the options |

### x-listbox:option

Used to specify an individual option.

| Attributes | Description |
|------------|-------------|
| value | The value of the option |
| disabled | A boolean used to disable the option |

### $listboxOption

A magic variable that exposes information about the current state of the option (element containing x-listbox:option).

| Properties | Description |
|------------|-------------|
| isActive | A boolean used to determine whether or not an option is currently active |
| isSelected | A boolean used to determine whether or not an option is currently selected |
| isDisabled | A boolean used to determine whether or not an option is currently disabled |

### x-listbox:label

Used to specify a custom label for the Listbox.