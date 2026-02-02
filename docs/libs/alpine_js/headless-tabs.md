# Tabs Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-tabs>
    <div x-tabs:list>
        <button x-tabs:tab>Tab 1</button>
        <button x-tabs:tab>Tab 2</button>
        <button x-tabs:tab>Tab 3</button>
    </div>

    <div x-tabs:panels>
        <div x-tabs:panel>Tab Panel 1</div>
        <div x-tabs:panel>Tab Panel 2</div>
        <div x-tabs:panel>Tab Panel 3</div>
    </div>
</div>
```

## Styling the selected tab

You can apply custom styling to the selected tab by using the $tab.isSelected boolean and setting any classes you need.

```html
<div x-tabs:list>
    <button x-tabs:tab :class="$tab.isSelected && 'active'">Tab 1</button>
    ...
</div>
```

## Disabling a tab

You can disable a tab by adding the disabled attribute to a x-tabs:tab element. This will make this tab un-selectable and will be skipped when navigating through tabs using the arrow-keys.

```html
<div x-tabs:list>
    <button x-tabs:tab disabled>Tab 1</button>
    ...
</div>
```

You can also access the disabled state of a tab anywhere inside that tab using $tab.isDisabled like so:

```html
<div x-tabs:list>
    <button x-tabs:tab disabled :class="$tab.isDisabled && 'disabled'">
        Tab 1
    </button>
    ...
</div>
```

## Manually activating tabs

By default, users can switch between tabs using the arrow keys (when focused on the tabs list). If you instead wish to allow them to navigate the tabs and only select a tab once they press the Enter or Space keys, you can add the manual attribute to the x-tabs element.

```html
<div x-tabs manual>
    ...
</div>
```

## Specifying the default tab

You can specify the default selected tab when the page loads by using the default-index attribute on the x-tabs element.

```html
<div x-tabs default-index="1">
    <div x-tabs:list>
        <button x-tabs:tab>Tab 1</button>
        <button x-tabs:tab>Tab 2</button>
        <button x-tabs:tab>Tab 3</button>
    </div>
    ...
</div>
```

## Controlling the selected tab

If you wish to programatically control which tab is currently selected, you can do so using x-model on the x-tabs element and binding to a value in the outer scope.

```html
<div x-data="{ selectedTabIndex: 0 }">
    <button @click="selectedTabIndex++">Next Tab</button>

    <div x-tabs x-model="selectedTabIndex">
        ...
    </div>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| Arrow Keys | Selects the next/previous non-disabled tab |
| Home/PageUp | Selects the first non-disabled tab |
| End/PageDown | Selects the last non-disabled tab |
| Enter/Space | Activates the selected tab when manual is set |

## API Reference

### x-tabs

The main directive for the Tabs component, used to contain the behavior for a group of tabs and panels.

| Attributes | Description |
|------------|-------------|
| default-index | An integer to set the default selected tab index |
| x-model | Used to control which tab is currently selected using outside data |
| manual | A boolean (defaults to false) that allows a user to navigate between tabs without selecting them |

### x-tabs:list

Used to specify the element containing the individual tabs.

### x-tabs:tab

Used to specify an individual tab.

### $tab

A magic variable that exposes information about the current state of the closest tab.

| Properties | Description |
|------------|-------------|
| isSelected | A boolean used to determine whether or not a tab is currently selected |
| isDisabled | A boolean used to determine whether or not a tab is currently disabled |

### x-tabs:panels

Used to specify a group of tab panels.

### x-tabs:panel

Used to specify an individual tab panel.

### $panel

A magic variable that exposes the current state of the tab panel.

| Properties | Description |
|------------|-------------|
| isSelected | A boolean used to determine whether or not a tab panel is selected |