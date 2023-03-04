const accountTemplate = `<div class="account" id="{ID}" ready="False" type="???" actionLocked="locked">
<input class="mw160px w15percentage" type="text" id="name" placeholder="Nome" title="Nome">
<input class="required mw160px w15percentage" ready="False" type="number" id="value" placeholder="Valor" title="Valor">
<input class="mw300px w50percentage" type="text" id="product" placeholder="Produto" title="Produto">
<input class="mw160px w12percentage" type="text" id="method" placeholder="Método" title="Método">
<input class="required mw35px w5percentage" ready="False" type="text" id="start" placeholder="Parcela Atual (Numérico ou INF)" title="Parcela Atual (Numérico ou INF)">
<input class="required mw35px w5percentage" ready="False" type="text" id="end" placeholder="Parcela Final (Numérico ou INF)" title="Parcela Final (Numérico ou INF)">
<input class="mw50px w5percentage" type="number" id="date" placeholder="Dia" title="Dia">
</div>`

const accountTemplateFrezze = `<div class="account freeze" id="{ID}" ready="False" type="???">
<input readonly type="text" id="name" placeholder="Nome" title="Nome">
<input readonly class="required" ready="False" type="number" id="value" placeholder="Valor" title="Valor">
<input readonly type="text" id="product" placeholder="Produto" title="Produto">
<input readonly type="text" id="method" placeholder="Método" title="Método">
<input readonly class="required" ready="False" type="text" id="start" placeholder="Parcela Atual (Numérico ou INF)" title="Parcela Atual (Numérico ou INF)">
<input readonly class="required" ready="False" type="text" id="end" placeholder="Parcela Final (Numérico ou INF)" title="Parcela Final (Numérico ou INF)">
<input readonly type="number" id="date" placeholder="Dia" title="Dia">
</div>`