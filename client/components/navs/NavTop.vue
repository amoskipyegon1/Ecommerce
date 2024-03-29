<script setup lang="ts">
import { storeToRefs } from "pinia";
import { Dropdown } from "floating-vue";
import "floating-vue/dist/style.css";
import { useAppStore } from "~~/stores/appStore";
import { useAuthStore } from "~~/stores/authStore";

const authStore = useAuthStore();
const { is_logged_in } = storeToRefs(authStore);
const { heightPos } = storeToRefs(useAppStore());
const { onLogout } = useApollo();
const user_payload = useCookie("user_payload");
const refresh_token = useCookie("user_refresh_token");

const logoutUser = (): void => {
	authStore.updateIsLoggedIn();
	refresh_token.value = null;
	user_payload.value = null;
	onLogout();
};
</script>
<template>
	<nav class="w-full flex flex-col z-20 sticky top-0 dark:shadow-white/10 shadow-sm">
		<div v-if="heightPos < 1" class="w-full flex flex-col">
			<ContentsTopNav />
		</div>
		<div
			class="w-full hidden md:flex flex-col px-4 md:px-8 lg:px-20 2xl:px-44 pt-2.5 md:pt-3 pb-2.5 md:pb-0 backdrop-blur-[100px] bg-c-base/80 dark:bg-c-dark/90"
		>
			<div class="w-full flex flex-row justify-between">
				<NuxtLink to="/" class="flex flex-row items-center uppercase">
					<NuxtImg src="/logo.png" class="mr-1 max-h-[2rem] sm:max-h-[2.2rem] rounded-lg shadow opacity-90" />
					<small class="text-2xl sm:text-3xl tracking-wide font-bold dark:text-c-mode"
						><span class="text-custom dark:text-custom">S</span>hop</small
					>
				</NuxtLink>
				<!-- Search input -->
				<div class="block w-[50%] lg:w-[40%]">
					<label for="search" class="text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
					<div class="relative flex flex-row-reverse -space-x-px w-full">
						<button
							class="px-6 py-2.5 bg-neutral-100 hover:bg-custom dark:hover:bg-custom hover:text-c-base rounded-r border border-l-0 border-neutral-200 hover:border-custom dark:hover:border-custom transition-colors duration-200 dark:bg-c-dark dark:text-c-mode dark:border-neutral-600"
						>
							<div class="w-5 h-5">
								<IconsSearch />
							</div>
						</button>
						<input
							type="search"
							id="search"
							class="block w-full px-5 text-base text-gray-800 border border-gray-200 rounded-l bg-gray-50 focus:outline-none focus:border-custom dark:focus:border-custom dark:bg-inherit dark:border-neutral-600 dark:text-c-base"
							placeholder="Search products, brands and categories"
							required
						/>
					</div>
				</div>

				<!-- Toggle auth btns -->
				<div class="flex flex-row items-center gap-x-2 text-neutral-500 dark:text-neutral-400">
					<Transition mode="out-in">
						<div v-if="!is_logged_in" class="flex flex-row items-center gap-x-1 lg:gap-x-2">
							<NuxtLink
								to="/auth"
								class="px-3 sm:px-5 py-1 text-sm sm:text-base border border-neutral-300 dark:border-neutral-600 font-semibold text-neutral-500 dark:text-[#bbb] rounded"
							>
								Login
							</NuxtLink>
							<NuxtLink
								to="/auth/register"
								class="px-3 sm:px-5 py-1 text-sm sm:text-base bg-custom border border-custom font-semibold text-white rounded"
							>
								Register
							</NuxtLink>
						</div>
						<div v-else class="flex flex-row items-center gap-x-1 lg:gap-x-2">
							<Dropdown class="block relative">
								<button
									class="px-2.5 py-1 text-base flex flex-row gap-x-2 items-center border border-neutral-300 rounded hover:bg-white dark:text-c-mode dark:hover:text-custom dark:hover:bg-alt-dark dark:border-neutral-600"
								>
									<Icon name="mdi:account-check-outline" class="text-xl" />
									Account
									<Icon name="mdi:chevron-down" class="ml-0.5 text-lg" />
								</button>
								<template #popper>
									<div class="top-full right-0 w-[240px] bg-white shadow py-2 flex flex-col rounded dark:bg-alt-dark">
										<div class="w-full px-3 py-2 border-b border-neutral-200 dark:border-neutral-600">
											<h3 class="text-base text-neutral-800 font-medium">Welcome to The Shop!</h3>
										</div>
										<ul class="w-full flex flex-col">
											<li class="px-3 py-1.5 hover:bg-stone-100 cursor-pointer dark:hover:bg-c-dark">
												<div class="flex items-center gap-x-2 text-base text-neutral-700">
													<Icon name="mdi:account-outline" class="text-xl" />
													<span class="">My Account</span>
												</div>
											</li>
											<li class="px-3 py-1.5 hover:bg-stone-100 cursor-pointer dark:hover:bg-c-dark">
												<div class="flex items-center gap-x-2 text-base text-neutral-700">
													<Icon name="mdi:package-variant-closed" class="text-xl" />
													<span class="">My Orders</span>
												</div>
											</li>
											<li class="px-3 py-1.5 hover:bg-stone-100 cursor-pointer dark:hover:bg-c-dark">
												<div class="flex items-center gap-x-2 text-base text-neutral-700">
													<Icon name="mdi:heart-multiple-outline" class="text-xl" />
													<span class="">Wish List</span>
												</div>
											</li>
										</ul>
									</div>
								</template>
							</Dropdown>
							<button
								@click="logoutUser"
								type="button"
								class="px-3 sm:px-5 py-1 text-sm sm:text-base border border-neutral-300 dark:border-neutral-600 font-semibold text-neutral-500 dark:text-[#bbb] rounded"
							>
								Logout
							</button>
						</div>
					</Transition>
				</div>
			</div>
			<div class="w-full block mt-3 sm:mt-4 border-t border-neutral-200/60 dark:border-neutral-700">
				<div id="nav-links" class="w-full flex flex-row items-center justify-center gap-x-4 lg:gap-x-6">
					<NuxtLink :to="{ name: 'Home' }">
						<span> Home </span>
					</NuxtLink>
					<NuxtLink :to="{ name: 'Products' }">
						<span> All Products </span>
					</NuxtLink>
					<NuxtLink to="/shops">
						<span> Shops </span>
					</NuxtLink>
					<button>
						<span> Offers </span>
					</button>
					<NuxtLink :to="{ name: 'Category', params: { category: 'Men Clothing & Fashion' } }"
						><span>Men Clothing & Fashion</span></NuxtLink
					>
					<NuxtLink :to="{ name: 'Category', params: { category: 'Computer & Accessories' } }"
						><span>Computer & Accessories</span></NuxtLink
					>
				</div>
			</div>
		</div>
		<div
			class="mobile-nav md:hidden w-full flex flex-col px-4 py-2.5 backdrop-blur-[100px] bg-c-base/80 dark:bg-c-dark/90 items-center"
		>
			<Transition mode="out-in" name="slide-top">
				<div v-if="heightPos < 2" class="w-full flex flex-row justify-between">
					<NuxtLink to="/" class="flex flex-row items-center uppercase">
						<NuxtImg src="/logo.png" class="mr-1 max-h-[2rem] sm:max-h-[2.4rem] rounded-lg shadow opacity-90" />
						<small class="text-2xl sm:text-3xl tracking-wide font-bold dark:text-c-mode"
							><span class="text-custom">S</span>hop</small
						>
					</NuxtLink>

					<!-- Toggle auth btns -->
					<div class="flex flex-row items-center gap-x-2 text-neutral-500 dark:text-neutral-400">
						<Transition mode="out-in">
							<div v-if="!is_logged_in" class="flex flex-row items-center gap-x-1 lg:gap-x-2">
								<NuxtLink
									to="/auth"
									class="text-sm sm:text-base font-semibold text-neutral-700 px-3 py-0.5 hover:text-custom dark:text-c-mode dark:hover:text-custom transition-colors duration-200"
								>
									Login
								</NuxtLink>
								<NuxtLink
									to="/auth/register"
									class="px-3 sm:px-4 py-1 sm:py-2 text-sm sm:text-base border border-custom font-semibold text-custom rounded"
								>
									Register
								</NuxtLink>
							</div>
							<div v-else class="flex flex-row items-center gap-x-1 lg:gap-x-2">
								<Dropdown class="block relative">
									<button
										class="px-2 py-1 text-base flex flex-row gap-x-2 items-center border border-neutral-300 rounded hover:bg-white dark:text-c-mode dark:hover:text-custom dark:hover:bg-alt-dark dark:border-neutral-600"
									>
										<Icon name="mdi:account-check-outline" class="text-xl" />
										Account
										<Icon name="mdi:chevron-down" class="text-xl ml-0.5" />
									</button>
									<template #popper>
										<div class="top-full right-0 w-[240px] bg-white shadow py-2 flex flex-col rounded dark:bg-alt-dark">
											<div class="w-full px-3 py-2 border-b border-neutral-200 dark:border-neutral-600">
												<h3 class="text-base text-neutral-800 font-medium">Welcome to The Shop!</h3>
											</div>
											<ul class="w-full flex flex-col">
												<li class="px-3 py-1.5 hover:bg-stone-100 cursor-pointer dark:hover:bg-c-dark">
													<div class="flex items-center gap-x-2 text-base text-neutral-700">
														<Icon name="mdi:account-outline" class="text-xl" />
														<span class="">My Account</span>
													</div>
												</li>
												<li class="px-3 py-1.5 hover:bg-stone-100 cursor-pointer dark:hover:bg-c-dark">
													<div class="flex items-center gap-x-2 text-base text-neutral-700">
														<Icon name="mdi:package-variant-closed" class="text-xl" />
														<span class="">My Orders</span>
													</div>
												</li>
												<li class="px-3 py-1.5 hover:bg-stone-100 cursor-pointer dark:hover:bg-c-dark">
													<div class="flex items-center gap-x-2 text-base text-neutral-700">
														<Icon name="mdi:heart-multiple-outline" class="text-xl" />
														<span class="">Wish List</span>
													</div>
												</li>
											</ul>
											<div class="w-full py-1 border-t border-neutral-200 dark:border-neutral-600">
												<button
													class="flex flex-row gap-x-2 items-center text-neutral-700 px-3 py-1.5 text-start w-full hover:bg-stone-100 dark:hover:bg-c-dark dark:text-neutral-100"
												>
													<Icon name="mdi:logout-variant" class="text-lg" />
													<span>Logout</span>
												</button>
											</div>
										</div>
									</template>
								</Dropdown>
							</div>
						</Transition>
					</div>
				</div>
				<!-- Search input -->
				<div v-else class="block w-full px-4">
					<label for="search" class="text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
					<div class="relative flex flex-row-reverse -space-x-px w-full">
						<button
							class="px-5 py-2 bg-neutral-100 hover:bg-custom dark:hover:bg-custom hover:text-c-base rounded-r border border-l-0 border-neutral-200 hover:border-custom dark:hover:border-custom transition-colors duration-200 dark:bg-c-dark dark:text-c-mode dark:border-neutral-600"
						>
							<div class="w-5 h-5">
								<IconsSearch />
							</div>
						</button>
						<input
							type="search"
							id="search"
							class="block w-full pl-5 pr-0.5 text-sm text-gray-800 border border-gray-200 rounded-l bg-gray-50 focus:outline-none focus:border-custom dark:focus:border-custom dark:bg-inherit dark:border-neutral-600 dark:text-c-base"
							placeholder="Search products, brands and categories"
							required
						/>
					</div>
				</div>
			</Transition>
		</div>
	</nav>
</template>

<style scoped>
#nav-links button,
#nav-links a {
	@apply font-semibold text-neutral-700 px-2 py-2.5 dark:text-neutral-200 transition-colors duration-300;
}

#nav-links a.router-link-exact-active {
	@apply text-custom;
}

#nav-links a.router-link-exact-active {
	background-image: linear-gradient(#dd9933, #dd9933);
	background-position: 0% 100%;
	background-repeat: no-repeat;
	background-size: 100% 2px;
	transition: background-size 0.2s, padding 0.2s;
}
#nav-links button span,
#nav-links a span {
	@apply text-sm lg:text-base;
}
#nav-links button,
#nav-links a {
	@apply pr-3 cursor-pointer;
	background-image: linear-gradient(#dd9933, #dd9933);
	background-position: 0% 100%;
	background-repeat: no-repeat;
	background-size: 0% 2px;
	transition: background-size 0.2s, padding 0.2s;
}
#nav-links button:hover,
#nav-links a:hover {
	background-size: 100% 2px;
}

.slide-top-enter-from {
	@apply -translate-y-2 opacity-0;
}
.slide-top-enter-active {
	@apply transition duration-200;
}
.slide-top-leave-to {
	@apply opacity-0;
}
.slide-top-leave-active {
	@apply transition-opacity;
}
</style>
