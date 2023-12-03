def angular_magic_component_factory(input):
    return f'''
    This is the user request: '{input}'. 
    Parse the angular_magic_component following the below instruction.

    instructions: 
    '
        {instructions}
    '

    This is the angular_magic_component:
    '
        {angular_magic_component_template}.
    '
    '''


angular_magic_component_template = f'''
import {{Component [signal][[WritableSignal, signal]]}} from '@angular/core'
import {{[formControl][[FormControl]], [form][[FormGroup]]}} from '@angular/forms';

@Component({{
    selector: 'app-cat-component',
    standalone: true,
    template: `
        <p>Meoow!<\p>
    `,
    styles: ``
}})
export class CatComponent {{
    [ signal ]
    [[ cat: WritableSignal<string>=signal('meoow'); ]]
    [ formControl ]
    [[ catControl = new FormControl<any>(''); ]]
    [ form ]
    [[ catGroup = new FormGroup<any>({{}}); ]]
}}
'''

instructions='''
In the request there are keys. 
In the request there is the name. if there isn't the name is ALWAYS cat-litter
In the request there is the prefix. if there isn't a prefix the prefix is ALWAYS app
The pascalname is equal to the name but in PascalCase and ends with 'Component'.
In the angular_magic_component there are string between single square, example [string]. these are the magic_keys. And string between double square, example [[string]]. these are magic_code.

If a magic_keys is among the keys, remove the key, and leave ONLY the CODE without square brackets.
if a magic_keys isn't among the keys, remove the magic_key and the associated magic_code from angular_magic_component

This is an example of angular_magic_component: 
'
    import {Component} from '@angular/core'
    [ meow ]
    [[ import { mad cat } from '@everywhere' ]] 

    @Component({{
        selector: '[prefix]-[name]',
        standalone: true,
        template: `
            <p>Meoow!<\p>
        `,
        styles: ``
    }})
    export class [pascalname] {{
        [ meow ]
        [[ i'm a cat ]]
        [ pur ]
        [[ pur things ]] 
    }}
'

if in the magic_keys there is only key meow, and the name is 'cat' the answer should be:
'
    import {Component} from '@angular/core'
    import { cats } from '@everywhere'

    @Component({{
        selector: 'app-cat-component',
        standalone: true,
        template: `
            <p>Meoow!<\p>
        `,
        styles: ``
    }})
    export class CatComponent {{
        i'm a cat
    }}
'
if the magic_keys are empty, the answer should be:
'
    import {{Component}} from '@angular/core'

    @Component({{
        selector: 'app-cat-component',
        standalone: true,
        template: `
            <p>Meoow!<\p>
        `,
        styles: ``
    }})
    export class CatComponent {{}}
'

'''