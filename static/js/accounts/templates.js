const accountTemplate = `<div class="account" id="{ID}" ready="False" type="???" actionLocked="locked">
<input class="mw160px w15percentage" type="text" id="name" placeholder="Name" title="Name">
<input class="required mw160px w15percentage" ready="False" type="number" id="value" placeholder="Value" title="Value">
<input class="mw300px w50percentage" type="text" id="product" placeholder="Product" title="Product">
<input class="mw160px w12percentage" type="text" id="method" placeholder="Method" title="Method">
<input class="required mw35px w5percentage" ready="False" type="text" id="start" placeholder="Current Installment (Numeric or INF)" title="Current Installment (Numeric or INF)">
<input class="required mw35px w5percentage" ready="False" type="text" id="end" placeholder="Final Installment (Numeric or INF)" title="Final Installment (Numeric or INF)">
<input class="mw50px w5percentage" type="number" id="date" placeholder="Day" title="Day">
</div>`

const accountTemplateFrezze = `<div class="account freeze" id="{ID}" ready="False" type="???">
<input readonly type="text" id="name" placeholder="Name" title="Name">
<input readonly class="required" ready="False" type="number" id="value" placeholder="Value" title="Value">
<input readonly type="text" id="product" placeholder="Product" title="Product">
<input readonly type="text" id="method" placeholder="Method" title="Method">
<input readonly class="required" ready="False" type="text" id="start" placeholder="Current Installment (Numeric or INF)" title="Current Installment (Numeric or INF)">
<input readonly class="required" ready="False" type="text" id="end" placeholder="Final Installment (Numeric or INF)" title="Final Installment (Numeric or INF)">
<input readonly type="number" id="date" placeholder="Day" title="Day">
</div>`